import json

from kafka import KafkaConsumer
from kafka import KafkaProducer

order_details_topic = "order_details"
order_confirmed_topic = "order_confirmed"

consumer = KafkaConsumer (
    order_details_topic, 
    bootstrap_servers="localhost:9092"
)

producer = KafkaProducer (
    bootstrap_servers="localhost:9092"
)

print("listening...")

while True:
    for message in consumer:
        received_message = json.loads(message.value.decode())
        print(received_message)

        user_id = received_message["user_id"]
        total_cost = received_message["total_cost"]
        # mocked email id for testing purpose
        email_id = f"{user_id}@gmail.com"

        data = {
            "customer_id" : user_id,
            "email_id" : email_id,
            "total_cost" : total_cost
        }

        producer.send(order_confirmed_topic, 
        json.dumps(data).encode("utf-8")
        )
        

