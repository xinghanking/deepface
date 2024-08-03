FROM python:latest
LABEL authors="LiuZhongLiang"
RUN mkdir /home/work
WORKDIR /home/work
RUN cd /home/work
COPY . .
RUN apt-get upgrade
RUN chmod +x bin/install.sh
RUN bin/install.sh
