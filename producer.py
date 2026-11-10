
from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

order = {
    "order_id": 101,
    "customer": "Chinmay",
    "product": "Laptop",
    "amount": 50000,
    "status": "ORDER_PLACED"
}

producer.send("orders", value=order)
producer.flush()

print("Order successfully sent to Kafka!")

producer.close()
