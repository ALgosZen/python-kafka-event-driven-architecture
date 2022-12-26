import json
from kafka import KafkaConsumer

order_confirmed_topic = "order_confirmed"

consumer = KafkaConsumer(
    order_confirmed_topic,
    bootstrap_servers="localhost:9092"
)

emails_sent_list = set()

while True:
    for message in consumer:
        consumed_message = json.loads(message.value.decode())
        cust_email = consumed_message["email_id"]
        print(f"sent email to: {cust_email}")
        emails_sent_list.add(cust_email)
        