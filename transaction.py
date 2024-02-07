import json
import time

from kafka import KafkaProducer,KafkaConsumer

ORDER_KAFKA_TOPIC = 'order_details'

consumer = KafkaConsumer(
    ORDER_KAFKA_TOPIC,
    bootstrap_servers="localhost:9092"
)

producer = KafkaProducer(
    bootstrap_servers="localhost:9092"
)

print("Going to start listening..")

while True:
    for message in consumer:
        print("Ongoing transaction...")
        consumed_message =json.loads(message.value.decode())
        print(consumed_message)
        