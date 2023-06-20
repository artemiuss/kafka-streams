#!/bin/bash

docker compose up -d
while [ ! -f "screenshots.png" ]; do sleep 1; done
docker compose down
