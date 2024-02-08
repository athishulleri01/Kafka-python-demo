from confluent_kafka import Producer

# Producer Example
producer_conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(producer_conf)
producer.produce('demoTopic', key='key', value='value')
producer.flush()