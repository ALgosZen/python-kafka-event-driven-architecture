# python-kafka-event-driven-architecture
scalable event driven architecture in python using apache kafka 
### Apache kafka is distributed event store and processing engine, written in java and scala.Kafka was originally developed at LinkedIn, and was subsequently open sourced in early 2011 
##### What is Apache Kafka?
###### Apache Kafka is a perfect match for building asynchronous, loosely-coupled event-driven architecture. Events trigger processing logic, which can be implemented in a more traditional as well as in a stream processing fashion. Architects must carefully choose between a request-driven and event-driven communication as per on their needs. To meet the primary goal of a Microservices architecture, modern stream processing system can be used to hold state both internally as well as in a database and how this state can be used to further increase independence of other services.

![Confluent Kafka](/images//image4.png?raw=true "Kafka")

> confluent is a cloud native kafka service vendor providing deployments across 3 major cloud vendors - google cloud, aws and azure.
![Confluent Kafka](/images//image2.png?raw=true "Confluent")
> A Cool tutorial on python 
[This is an external link to conflient tutorials](https://developer.confluent.io/get-started/python/)

sample ordering system system using event driven architecture
![Ordering Flow](/images//image6.png?raw=true "Orders")

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

> The consumer will wait indefinitely for new events. You can kill the process or continue streaming messages using producer.

kafka event driven  architecture is scalable 

** the end ** 



