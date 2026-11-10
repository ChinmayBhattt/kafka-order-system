
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "orders",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("Waiting for orders...")

for message in consumer:
    order = message.value

    print("\nNew Order Received!")
    print("Order ID:", order["order_id"])
    print("Customer:", order["customer"])
    print("Product:", order["product"])
    print("Amount:", order["amount"])
    print("Status:", order["status"])
