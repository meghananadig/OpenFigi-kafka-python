# import kafka
# #from main import *
# from kafka import KafkaProducer
#
#
# producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
#
# try:
#     #producer.send('OpenFIGI', value=response_result_set)
#     producer.send('OpenFIGI', b"Hello from kafka...")
# except():
#     print("error")
# #producer.send(response_json);

from time import sleep
from json import dumps
from kafka import KafkaProducer
from callapi import *
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

producer.send('OpenFIGI', value=response_result_set)
sleep(0.5)
producer.flush();