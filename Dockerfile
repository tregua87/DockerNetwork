FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install wget -y

RUN mkdir -p /home/peer
COPY . /home/peer/

CMD wget 172.20.0.22:2222/add; sleep 50
