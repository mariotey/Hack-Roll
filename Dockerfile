# base image  
FROM python:3.11.4  
# setup environment variable  
# set work directory  

# where your code lives 

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  
RUN pip install django requests
# copy whole project to your docker home directory. 
COPY . .  
# run this command to install all dependencies  

# port where the Django app runs  cd 
EXPOSE 8000  
# start server  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]