# Data Streaming Homework - Kafka Streaming

Goals:
- Learn about implementation of a simple kafka streaming application

Instructions:
- Prepare a dataset: export a history from your favorite browser to a CSV file
- Prepare a kafka (redpanda) environment. 
- Implement a “generator” microservice that splits the dataset to messages, sends them to kafka as a message. 
- Implement a kafka streaming application that calculates a visiting statistic - a number of visits for each root domain (com, ua, org, edu, etc) from your browser history and prints top five root domains

## Instructions on how to run the implementation

Set up
```
git clone https://github.com/conduktor/kafka-stack-docker-compose.git
cd kafka-stack-docker-compose
docker compose -f full-stack.yml up -d
cd ..
git clone https://github.com/artemiuss/kafka_throughput_investigation.git
cd kafka_throughput_investigation
docker compose build
```

Run streaming application
```
./run_stream.sh
```

Stop and clean-up
```
docker compose down --rmi all -v --remove-orphans
cd ../kafka-stack-docker-compose
docker compose -f full-stack.yml down --rmi all -v --remove-orphans
```

## Screenshots of your top five domains

![Screenshots](screenshots.png)
