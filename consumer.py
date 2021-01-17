from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'sf.pd.cfs',
     bootstrap_servers="localhost:9092",
     auto_offset_reset='earliest',
     group_id='0')

for message in consumer:
    if message is not None:
        print(message.value.decode('utf-8'))