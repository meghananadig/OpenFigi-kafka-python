import sqlalchemy as db
import os
import json
import logging
import psycopg2

#Postgres variables
# host_server = str(os.environ.get('host_server', 'localhost'))
# db_server_port = str(os.environ.get('db_server_port', '5432'))
# database_name = str(os.environ.get('database_name'))
# db_username = str(os.environ.get('db_username'))
# db_password = str(os.environ.get('db_password'))
database_name = "postgres"
db_username = "postgres"
db_password = "admin"
host_server = 'localhost'
db_server_port = 5442
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}'.format(db_username, db_password, host_server, db_server_port, database_name)
FASTAPI_DB_URL = 'postgresql://{}:{}@{}:{}/{}'.format(db_username, db_password, 'db', 5432, database_name)
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

def fastapi_connect():
    global engine
    global connection
    global metadata
    engine = db.create_engine(FASTAPI_DB_URL)
    connection = engine.connect()
    metadata = db.MetaData()
    print("Database connection established successfully for fast api!")


def getSecurityByType(securityType):
    securities = db.Table('securities', metadata, autoload=True, autoload_with=engine)
    query = db.select([securities]).where(securities.columns.securitytype == securityType)
    result = connection.execute(query)
    return [dict(r) for r in result]

def insertData(figi, securityType, marketSector, ticker, name, exchCode, shareClassFIGI, compositeFIGI, securityType2, securityDescription):
    securities = db.Table('securities', metadata, autoload=True, autoload_with=engine)
    query = db.insert(securities).values(figi=figi, securitytype=securityType, marketsector=marketSector, ticker=ticker,
                                         name=name, exchcode=exchCode, shareclassfigi=shareClassFIGI, compositefigi=compositeFIGI,
                                         securitytype2=securityType2, securitydescription=securityDescription)
    connection.execute(query)
    print(query)

def disconnect():
    connection.close()
    engine.dispose()