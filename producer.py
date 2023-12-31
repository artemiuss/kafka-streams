#!/usr/bin/env python3
import os, csv, json, time
from kafka import KafkaProducer
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    DS_FILENAME = os.getenv("DS_FILENAME")
    KAFKA_HOST = os.getenv("KAFKA_HOST")
    KAFKA_PORT = os.getenv("KAFKA_PORT")
    KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

    producer = KafkaProducer(bootstrap_servers=[f"{KAFKA_HOST}:{KAFKA_PORT}"])

    with open(DS_FILENAME, encoding="utf8", newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            json_data = json.dumps(row).encode('utf-8')
            print(json_data)
            producer.send(topic=KAFKA_TOPIC, value=json_data)
            time.sleep(1)
        producer.flush()

    producer.close()

if __name__ == '__main__':
    main()
