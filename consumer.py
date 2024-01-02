from kafka import KafkaConsumer

bootstrap_servers = 'localhost:9092'
topic = 'msg'
username = 'consumer'
password = 'consumer-secret'

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    api_version=(0,11,5),
    security_protocol='SASL_PLAINTEXT',
    sasl_mechanism='PLAIN',
    sasl_plain_username='consumer',
    sasl_plain_password='consumer-secret',
    auto_offset_reset='earliest'
)

# Consume messages
for message in consumer:
    print('Received message: {}'.format(message.value.decode('utf-8')))

# Close the consumer
consumer.close()

