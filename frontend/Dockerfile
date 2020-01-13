FROM node:13.6-alpine
MAINTAINER Benning

RUN npm install -g @vue/cli

RUN mkdir /frontend
WORKDIR /frontend
COPY . /frontend
RUN npm install

RUN adduser -D user
USER user