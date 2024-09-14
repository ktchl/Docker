#!/bin/bash
echo "image fastapi"
docker image pull datascientest/fastapi:1.0.0

echo "image authentification"
PATH_AUTHENTIFICATION="/home/ubuntu/exam_docker_TANCHALEUNE/test_authentification/"
TAG="latest"
IMAGE_AUTHENTIFICATION="authentification"
docker build -t "$IMAGE_AUTHENTIFICATION:$TAG" "$PATH_AUTHENTIFICATION"

echo "image authorization"
PATH_AUTHORIZATION="/home/ubuntu/exam_docker_TANCHALEUNE/test_authorization/"
TAG="latest"
IMAGE_AUTHORIZATION="authorization"
docker build -t "$IMAGE_AUTHORIZATION:$TAG" "$PATH_AUTHORIZATION"

echo "image content"
PATH_CONTENT="/home/ubuntu/exam_docker_TANCHALEUNE/test_content/"
TAG="latest"
IMAGE_CONTENT="content"
docker build -t "$IMAGE_CONTENT:$TAG" "$PATH_CONTENT"

echo "Création dossier data"
mkdir data

echo "Lancement docker-compose up"
docker-compose up 2>&1 | tee log.txt

