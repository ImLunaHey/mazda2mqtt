# mazda2mqtt
**Publish all myMazda Car Data to MQTT**

---
># !! ATTENTION !!!
>***A too frequent refresh of the data can drain your 12V starter battery of the car.  
So use this Program at your own risk***
---

This Program uses an [unofficial API by bdr99](https://github.com/bdr99/node-mymazda), and it may stop working at any time without warning.

Prerequisites:
1. Set up your Car in the mymazda app.
2. Create a second Driver for mazda2mqtt.

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
```
docker run -d --name mazda2mqtt --restart unless-stopped -v <YOUR_DIR/config.yaml>:/usr/src/app/config.yaml mazda2mqtt:latest
```
---
**MQTT-API**

To trigger a manual refresh for one car, publish the following via MQTT:  
(replace < VIN > with the VIN of the Car)
```
mazda2mqtt/SET/<VIN>/refresh
```

---
### History:

| Date | Change                                                        |
|-------|---------------------------------------------------------------|
|26.04.2023| Initial Version                                               |
|03.06.2023| only one refresh at the beginning because risk of battery dry |
|xx.06.2023| refresh Data via MQTT                                         |

