# OpenFigi-kafka-python

This project streams search data from Open FIGI API based on security name and exchange code. It then sends the data to Kafka using Kafka Producer.
The messages are consumed from Kafka Consumer into Postgres DB using Python.
Fast API is exposed from the Postgre DB for consumption of requested data.

Work in Progress.
