# base image  
FROM python:3.9

# setup environment variable  
ENV src=/home/src

# set work directory  
RUN mkdir -p $src  
# copy whole project to your docker home directory. 
COPY . $src 

# where your code lives  
WORKDIR $src  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  
# run this command to install all dependencies
RUN pip install -r requirements.txt  
 
# port where the Django app runs  
EXPOSE 8000

# start server  
RUN python http_monitor/manage.py makemigrations
RUN python http_monitor/manage.py migrate

# health checking and run server
CMD python http_monitor/manage.py healthcheck 1 & python http_monitor/manage.py runserver 0.0.0.0:8000
