FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt update -y

RUN apt upgrade -y

RUN apt install python3 -y

RUN apt install python3-pip -y

RUN pip3 install opencv-python

RUN pip3 install python-twitch-stream

RUN apt install ffmpeg -y

RUN pip3 install keyboard

RUN pip3 install rovlib

WORKDIR /twitch

