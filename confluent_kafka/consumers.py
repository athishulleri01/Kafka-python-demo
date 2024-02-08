from confluent_kafka import Consumer

# Consumer Example
consumer_conf = {'bootstrap.servers': 'localhost:9092', 'group.id': 'my_group', 'auto.offset.reset': 'earliest'}
consumer = Consumer(consumer_conf)
consumer.subscribe(['demoTopic'])

while True:
    msg = consumer.poll(1.0)  # Adjust the timeout as needed
    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue
    print(f"Received message: {msg.value().decode('utf-8')}")



# Consumer Example