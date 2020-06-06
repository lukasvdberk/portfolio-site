
# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM debian:stretch
FROM python:3.8

RUN apt-get install default-libmysqlclient-dev

# Initialize directory
RUN mkdir /personal_site
WORKDIR /personal_site
ADD ./personal_site /personal_site

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

# Needed for mysql
RUN apt-get install python-dev python3-dev
CMD pip install MySQL-python
RUN pip install pymysql
RUN pip install mysqlclient

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt