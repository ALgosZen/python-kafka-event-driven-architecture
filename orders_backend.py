import json
import time
from random import choice,choices
from kafka import KafkaProducer, producer

topic = "order_details"
order_limit = 15
items = ['burger', 'sandwitch', 'donut', 'bagle', 'cream']


producer = KafkaProducer(bootstrap_servers="localhost:9092")

print("going to generate orders in 10 secs interval")

for i in range(1, order_limit):
    data = {
        "order_id" : i,
        "user_id"  : f"tom_{i}",
        "total_cost" : i * 5,
        "items" : choices(items, k=2)
    }
    producer.send(
        topic, json.dumps(data).encode("utf-8")
    )
    print(f"done sending..{i}")
    time.sleep(10)






