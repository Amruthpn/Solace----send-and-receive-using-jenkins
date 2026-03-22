import solace.messaging.messaging_service as messaging_service
from solace.messaging.resources.topic import TopicSubscription

service = messaging_service.MessagingService.builder() \
    .from_properties({
        "solace.messaging.transport.host": "your-host",
        "solace.messaging.service.vpn-name": "default",
        "solace.messaging.authentication.scheme": "basic",
        "solace.messaging.authentication.basic.username": "your-username",
        "solace.messaging.authentication.basic.password": "your-password"
    }).build()

service.connect()

receiver = service.create_direct_message_receiver_builder() \
    .with_subscriptions(TopicSubscription.of("demo/event")) \
    .build()

receiver.start()

print("Listening for messages...")

while True:
    msg = receiver.receive_message()
    print("Received:", msg.get_payload_as_string())
