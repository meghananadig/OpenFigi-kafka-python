
from kafka import KafkaConsumer
from json import loads
from time import sleep
from repo import connect as connect
from repo import insertData as insertData
consumer = KafkaConsumer(
    'OpenFIGI',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='1',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
    )
for events in consumer:

    var = (events[6])
    #connect to db
    connect()
    #insert data
    dict_res = var[0]
    insertData(dict_res['figi'], dict_res['securityType'], dict_res['marketSector'], dict_res['ticker'], dict_res['name'], dict_res['exchCode'], dict_res['shareClassFIGI'], dict_res['compositeFIGI'], dict_res['securityType2'], dict_res['securityDescription'])




