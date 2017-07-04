FROM mongo:latest

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY requirements.txt /usr/src/app/
RUN apt-get install Flask mongoengine pika
#RUN pip install -i requirements.txt

# Bundle app source
COPY . /usr/src/app

EXPOSE 8080
CMD [ "python", "monitors.py" ]

