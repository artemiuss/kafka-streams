#!/usr/bin/env python3
import os, urllib
from dotenv import load_dotenv
from kaflow import (
    Kaflow,
    FromValue,
    Json
)
from pydantic import BaseModel

def main():
    load_dotenv()

    KAFKA_HOST = os.getenv("KAFKA_HOST")
    KAFKA_PORT = os.getenv("KAFKA_PORT")
    KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

    class URL(BaseModel):
        URL: str

    app = Kaflow(brokers=f"{KAFKA_HOST}:{KAFKA_PORT}")

    root_domain_dict = {}

    @app.consume(topic=KAFKA_TOPIC)
    async def consume_url(
        message: FromValue[Json[URL]]
    ):
        root_domain = urllib.parse.urlparse(message.URL).netloc.split('.')[-1]
        if root_domain in root_domain_dict:
            root_domain_dict[root_domain] += 1
        else:
            root_domain_dict[root_domain] = 1

        root_domain_list = sorted(root_domain_dict.items(), key=lambda x: x[1], reverse=True)[:5]
        print(', '.join(str(f"{x[0]} - {x[1]}") for x in root_domain_list))

    app.run()

if __name__ == '__main__':
    main()
