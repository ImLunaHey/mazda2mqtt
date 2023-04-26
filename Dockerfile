FROM python:3.9-slim

# Working directory for the application
WORKDIR /usr/src/app

# Set Entrypoint with hard-coded options
ENTRYPOINT ["python3", "./mazda2mqtt.py"]

COPY requirements.txt /usr/src/app/

RUN apt update && apt install -y build-essential \
 && pip3 install --no-cache-dir -r requirements.txt \
 && apt purge -y --auto-remove build-essential && apt clean

# Copy everything to the working directory (Python files, templates, config) in one go.
COPY . /usr/src/app/