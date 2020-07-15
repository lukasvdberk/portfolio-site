
# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM debian:stretch
FROM python:3.8

RUN apt-get install default-libmysqlclient-dev

# Initialize directory
RUN mkdir /personal_site_app
WORKDIR /personal_site_app
ADD ./ /personal_site_app

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip

# Needed for mysql
CMD pip3 install MySQL-python
RUN pip3 install pymysql
RUN pip3 install mysqlclient
# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt