import sqlalchemy as db
import os
import json
import logging

#Postgres variables
host_server = str(os.environ.get('host_server', 'localhost'))
db_server_port = str(os.environ.get('db_server_port', '5432'))
database_name = str(os.environ.get('database_name'))
db_username = str(os.environ.get('db_username'))
db_password = str(os.environ.get('db_password'))
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}'.format(db_username, db_password, host_server, db_server_port, database_name)
print(DATABASE_URL)
#establish connection
def connect():
    global engine
    global connection
    global metadata
    engine = db.create_engine(DATABASE_URL)
    connection = engine.connect()
    metadata = db.MetaData()
    print("Database connection established successfully!")

def getSecurityByType(securityType):
    securities = db.Table('securities', metadata, autoload=True, autoload_with=engine)
    query = db.select([securities]).where(securities.columns.securitytype == securityType)
    result = connection.execute(query)
    return [dict(r) for r in result]

def disconnect():
    connection.close()
    engine.dispose()