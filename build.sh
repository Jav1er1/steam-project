#!/bin/bash

echo "========================="
echo "CREANDO IMAGEN"
echo "========================="

docker build -t steamapp .

echo "========================="
echo "BORRANDO CONTENEDOR"
echo "========================="

docker stop samplerunning || true
docker rm samplerunning || true

echo "========================="
echo "EJECUTANDO CONTENEDOR"
echo "========================="

docker run --name samplerunning \
-e STEAM_API_KEY=$STEAM_API_KEY \
-e STEAM_ID=$STEAM_ID \
steamapp

echo "========================="
echo "DOCKER PS"
echo "========================="

docker ps -a

