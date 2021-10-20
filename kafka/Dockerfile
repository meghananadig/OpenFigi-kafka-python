
FROM python:3.9


WORKDIR /code


COPY ./kafka/requirements.txt .


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./kafka/kafkaProducer.py .
COPY ./kafka/main.py .
COPY ./fastapi .

#COPY ./kafka/run.sh ./

#RUN chmod a+x run.sh

CMD ["python3", "kafkaProducer.py"]
