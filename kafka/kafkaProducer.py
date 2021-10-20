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
from main import *
import sys
from kafka import KafkaConsumer
import json
from app import *


print("producer sleeping for 10s")
#sleep(10)
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    api_version=(0, 10, 1),
    value_serializer=lambda x: dumps(x).encode('utf-8')
)
try:
    producer.send('OpenFIGI', value=response_result_set[1])
    print(response_result_set[1], "response_result_set[1]")
except Exception:
    print("producer error", Exception)
print("producer exiting")

#Consumer
print("consumer sleeping for 20s")
#sleep(20)
consumer = KafkaConsumer(
    'OpenFIGI',
    bootstrap_servers=['kafka:9092'],
    api_version=(0, 10, 1),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='1',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )


print("outside consumer")
print("event in consumer", consumer)
for event in consumer:
    print('FROM CONSUMER')
    var = (event[6][0])
    print(var)
    #connect to db
    db_repo.connect()
    #insert data
    db_repo.insertData(var['figi'], var['securityType'], var['marketSector'], var['ticker'], var['name'], var['exchCode']
                       , var['shareClassFIGI'], var['compositeFIGI'], var['securityType2'], var['securityDescription'])

    print('FROM CONSUMER', var['figi'])

# sys.exit(0)

