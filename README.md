# Kafka-python-demo
$ sudo systemctl start zookeeper
$ sudo systemctl start kafka

sudo systemctl status zookeeper
$ sudo systemctl status kafka

 Create a Kafka Topic
 ........................
With Kafka and all components installed, we will create a topic and try to send a message. In Kafka, a topic is a fundamental unit used to organize messages. 
Each topic should have a unique name across a cluster. Topics allow users to send and read data between Kafka servers.

You can create as many clusters as you want in Kafka. That said, Now let’s create a Topic called sampleTopic on localhost port 9092 with a single replication factor.

cd /usr/local/kafka
$ bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic sampleTopic


Let us break down the command:

–create: Creates a new topic
–replication-factor: Specifies how many copies of data will be created
–partitions: Specifies the number of partitions as the number of brokers by which your data will be split
–topic: Specifies the name of the topic. Topics are split into several partitions.
.............................................


As mentioned earlier, you can create as many topics as you can using the same syntax. To check or list the topics created, run the command:

$ bin/kafka-topics.sh --list --bootstrap-server localhost:9092
..................................................

Send and Receive a Message in Kafka
In Kafka, a ‘producer’ is an application that writes data into topics across different partitions. Applications integrate a Kafka client library to write a message to Apache Kafka. Kafka client libraries are diverse and exist for a myriad of programming languages including Java, Python among others.

Let us now run the producer and generate a few messages on the console.

$ bin/kafka-console-producer.sh --broker-list localhost:9092 --topic sampleTopic
..................................................

Once you are done, you can exit or keep the terminal running. To consume the messages, open a new terminal and run the following command:

$ bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sampleTopic --from-beginning

