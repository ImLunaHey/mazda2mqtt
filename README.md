# mazda2mqtt
Publish all myMazda Car Data to MQTT

## Installation Guide:
Clone the git repository.  
Create a virtual environment and install the requirements:  
```
apt install python-virtualenv
virtualenv -p python3 ~/mazda2mqtt.env
source ~/myzda2mqtt.enc/bin/acrivate
cd mazda2mqtt 
pip3 install -r requirements.txt
```

or build a Docker Image
```
docker build https://github.com/C64Axel/mazda2mqtt.git#dev -t mazda2mqtt:latest
```