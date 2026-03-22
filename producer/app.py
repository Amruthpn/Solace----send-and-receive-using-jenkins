import solace.messaging.messaging_service as messaging_service
from solace.messaging.resources.topic import Topic

service = messaging_service.MessagingService.builder() \
    .from_properties({
        "solace.messaging.transport.host": "your-host",
        "solace.messaging.service.vpn-name": "default",
        "solace.messaging.authentication.scheme": "basic",
        "solace.messaging.authentication.basic.username": "your-username",
        "solace.messaging.authentication.basic.password": "your-password"
    }).build()

service.connect()

publisher = service.create_direct_message_publisher_builder().build()
publisher.start()

topic = Topic.of("demo/event")

message = service.message_builder().build("Hello from Jenkins 🚀")

publisher.publish(message, topic)

print("Event sent!")
