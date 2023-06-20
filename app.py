#!/usr/bin/env python3
import os, csv, json, datetime
from kaflow import Kaflow
from dotenv import load_dotenv

def main():
    load_dotenv()

    KAFKA_HOST = os.getenv("KAFKA_HOST")
    KAFKA_PORT = os.getenv("KAFKA_PORT")
    KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

    app = Kaflow(name="AwesomeKakfaApp", brokers=f"{KAFKA_HOST}:{KAFKA_PORT}")

    print("Top five root domains:")

if __name__ == '__main__':
    main()
