# python-kafka-event-driven-architecture
scalable event driven architecture in python using apache kafka 
### Apache kafka is distributed event store and processing engine, written in java and scala.Kafka was originally developed at LinkedIn, and was subsequently open sourced in early 2011 
##### how kafka works?
![Confluent Kafka](/images//image3.png?raw=true "MSK")

> confluent is a cloud native kafka service vendor providing deployments across 3 major cloud vendors - google cloud, aws and azure.
![Confluent Kafka](/images//image2.png?raw=true "MSK")
> A Cool tutorial on python 
[This is an external link to conflient tutorials](https://developer.confluent.io/get-started/python/){:target="_blank"}


> Amazon MSK makes it easy to ingest and process streaming data in real time with fully managed Apache Kafka
![Amazon MSK](/images//image1.png?raw=true "MSK")

> For this exercise , lets run kafka locally using docker. 
1. create docker compose file or clone repo
2. make sure docker is running and run the following command to start the kafka service 
```
docker compose up -d
```
3. you should now find kafka and zookeeper running 
```
docker ps
```
4. run the following command to create kafka topic named **purchases**
(if you are using confluent or aws for kafka service or running kafka locally, you dont need this step. instead create topic using gui interface provided)
```
docker compose exec broker \
  kafka-topics --create \
    --topic purchases \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1
```
5. now create producer.py . you may have to install python package confluent_kafka using the command
```
pip install confluent_kafka
```

6. run producer py to send some events 
```
python producer.py getting_started.ini
```
7. run the consumer 
```
python consumer.py getting_started.ini

8. The consumer will wait indefinitely for new events. You can kill the process or continue streaming messages using producer.

9. this architecture is scalable 


