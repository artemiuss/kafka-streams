#!/usr/bin/env python3
import os, csv, json, datetime
import kaflow
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    DS_FILENAME = os.getenv("DS_FILENAME")
    KAFKA_HOST = os.getenv("KAFKA_HOST")
    KAFKA_PORT = os.getenv("KAFKA_PORT")
    KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

    print("Starting streamer...")

    print("Top five root domains:")

if __name__ == '__main__':
    main()
