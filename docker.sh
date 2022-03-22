#!/bin/bash

echo "build docker image ...."
docker build -t tictactoe:latest . 

echo "running docker image ...."
docker run -it -d -p 5000:5000 tictactoe




