# mazda2mqtt
Publish all myMazda Car Data to MQTT

## Installation Guide:
Clone the git repository.  
Create a virtual environment and install the requirements:  
```
apt install python-virtualenv
cd mazda2mqtt 

virtualenv -p python3 ../mazda2mqtt.env
source ../myzda2mqtt.env/bin/activate

pip3 install -r requirements.txt
```
Then copy config_example.yaml to config.yaml an insert your data.  
Start mazda2mqtt:
```
cd mazda2mqtt
source ../myzda2mqtt.env/bin/activate
python mazda2mqtt.py
```

Or build your own Docker Image
```
docker build https://github.com/C64Axel/mazda2mqtt.git#master -t mazda2mqtt:latest
```
Start the container with /usr/src/app/config.yaml mapped to the config file
