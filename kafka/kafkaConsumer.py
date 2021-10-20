import sys

import app.repo as db_repo


from kafka import KafkaConsumer
import json
from time import sleep

print("consumer sleeping for 20s")
sleep(20)
consumer = KafkaConsumer(
    'OpenFIGI',
    bootstrap_servers=['kafka:9092'],
    api_version=(0, 10, 1),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='1',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

#consumer.subscribe('OpenFIGI')
print("outside consumer")
print("event in consumer", consumer)
for event in consumer:
    print('FROM CONSUMER')
    var = (event[6][0])
    print(var)
    # #connect to db
    # db_repo.connect()
    # #insert data
    # db_repo.insertData(var['figi'], var['securityType'], var['marketSector'], var['ticker'], var['name'], var['exchCode']
    #                    , var['shareClassFIGI'], var['compositeFIGI'], var['securityType2'], var['securityDescription'])
    #
    # print('FROM CONSUMER', var['figi'])
print("nooooo")

