import solace.messaging.messaging_service as messaging_service
from solace.messaging.resources.topic import TopicSubscription

service = messaging_service.MessagingService.builder() \
    .from_properties({
        "solace.messaging.transport.host": "http://localhost:8080",
        "solace.messaging.service.vpn-name": "kafka-test",
        "solace.messaging.authentication.scheme": "basic",
        "solace.messaging.authentication.basic.username": "kafka-clientuser",
        "solace.messaging.authentication.basic.password": "kafka-clientuser"
    }).build()

service.connect()

receiver = service.create_direct_message_receiver_builder() \
    .with_subscriptions(TopicSubscription.of("KAFKA/SOLACE")) \
    .build()

receiver.start()

print("Listening for messages...")

while True:
    msg = receiver.receive_message()
    print("Received:", msg.get_payload_as_string())
