from kafka import KafkaProducer
from kafka.errors import KafkaError

bootstrap_servers = 'localhost:9092'
topic = 'msg'
username = 'producer'
password = 'producer-secret'

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    api_version=(0,11,5),
    security_protocol='SASL_PLAINTEXT',
    sasl_mechanism='PLAIN',
    sasl_plain_username='producer',
    sasl_plain_password='producer-secret'
)

# Produce a message

message_value = ['Hello', 'Kafka!','hi','upwork','kafka']
for i in message_value:
	message = i
	producer.send(topic, value=message.encode('utf-8'))

# Flush and close the producer
producer.flush()
producer.close()

