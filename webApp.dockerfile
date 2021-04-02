# Set base image (host OS)
FROM python:3.8-slim

# Copy the dependencies & app into the working directory in docker
COPY requirements.txt ./app/requirements.txt
COPY main.py ./app/main.py
COPY website ./app/website

# Install dependencies for docker
RUN cd ./app && pip3 install -r requirements.txt

# Specify the port number the container should expose
EXPOSE 5000

# Commands to run on container start
CMD ["python3", "./app/main.py"]
