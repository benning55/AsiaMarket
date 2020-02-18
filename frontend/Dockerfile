FROM node:13.7.0
MAINTAINER Benning

RUN mkdir /frontend
WORKDIR /frontend
COPY ./package.json /frontend
RUN npm install
COPY . /frontend

