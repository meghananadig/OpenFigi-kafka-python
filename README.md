# OpenFigi-kafka-python

This project streams search data from Open FIGI API based on security name and exchange code. The data is sent to Kafka using Kafka Producer.
The messages are consumed from Kafka Consumer into Postgres DB using Python.
Fast API is layered from the Postgre DB for consumption of requested data.

Coming up !
Apache Beam implementation for data processing.
