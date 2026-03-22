import solace.messaging.messaging_service as messaging_service
from solace.messaging.resources.topic import Topic

service = messaging_service.MessagingService.builder() \
    .from_properties({
        "solace.messaging.transport.host": "tcp://192.168.0.117:55555",
        "solace.messaging.service.vpn-name": "kafka-test",
        "solace.messaging.authentication.scheme": "basic",
        "solace.messaging.authentication.basic.username": "kafka-clientuser",
        "solace.messaging.authentication.basic.password": "kafka-clientuser"
    }).build()

service.connect()

publisher = service.create_direct_message_publisher_builder().build()
publisher.start()

topic = Topic.of("KAFKA/SOLACE")

message = service.message_builder().build("Hello from Jenkins 🚀")

publisher.publish(message, topic)

print("Event sent!")
