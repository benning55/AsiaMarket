FROM node:13.7.0
MAINTAINER Benning

RUN npm install -g @vue/cli

RUN mkdir /frontend
WORKDIR /frontend
COPY . /frontend
RUN npm install
