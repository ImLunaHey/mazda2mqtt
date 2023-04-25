import asyncio
import yaml
import paho.mqtt.publish as publish
import pymazda
from time import sleep

async def main() -> None:

    def create_msg(object, vehicleid, mqtt_topic, indent='/'):
        msg = []
        for key in object:
            if type(object[key]) == dict:
                create_msg(object[key], vehicleid, mqtt_topic, indent + key + '/')
            else:
                msg.insert(0, (mqtt_topic + '/' + str(vehicleid) + indent + key, object[key],1))

        publish.multiple(msg, hostname=mqtt_broker_address, port=mqtt_broker_port, client_id=mqtt_clientname,
                        auth=mqtt_auth)
        return msg

    # Read Config
    with open('config.yaml', 'r') as configfile:
        config = yaml.safe_load(configfile)

    status_wait = config['status']['wait'] or 30
    status_refreshwait = config['status']['refreshwait'] or 2

    # Connect to MQTT-Broker
    print('Initalize MQTT')
    mqtt_broker_address = config['mqtt']['host']
    mqtt_broker_port = config['mqtt']['port'] or 1883
    mqtt_broker_user = config['mqtt']['user'] or None
    mqtt_broker_password = config['mqtt']['password'] or None
    mqtt_topic = config['mqtt']['topic'] or 'mazda2mqtt'
    mqtt_clientname = config['mqtt']['clientname'] or 'mazda2mqtt'
    if not mqtt_broker_user:
        mqtt_auth = None
    else:
        mqtt_auth = {'username':mqtt_broker_user,'password':mqtt_broker_password}

    # Connect to myMazda
    print('Initialize myMazda')
    mazda_user = config['mazda']['user']
    mazda_password = config['mazda']['password']
    mazda_region = config['mazda']['region'] or 'MME'

    mazdaclient = pymazda.Client(mazda_user, mazda_password, mazda_region, use_cached_vehicle_list=True)

    # Get all Vehicles and publish base
    print('Get all vehicles')
    try:
        vehicles = await mazdaclient.get_vehicles()
    except Exception:
        raise Exception("Failed to get list of vehicles")

    # Publish vehicle data
    print('publish all vehicles data')
    for vehicle in vehicles:
        create_msg(vehicle,vehicle['vin'], mqtt_topic)

    try:
        while True:
            print('refresh all vehicles data and wait')
            for vehicle in vehicles:
                # refresh data
                await mazdaclient.refresh_vehicle_status(vehicle['id'])

            sleep(status_refreshwait * 60)

            print('publish all vehicles status')
            for vehicle in vehicles:
                # publish vehicle status
                vehicle_status = await mazdaclient.get_vehicle_status(vehicle['id'])
                create_msg(vehicle_status, vehicle['vin'], mqtt_topic)

                # publish vehicle ev status
                vehicle_ev_status = await mazdaclient.get_ev_vehicle_status(vehicle['id'])
                create_msg(vehicle_ev_status, vehicle['vin'], mqtt_topic)

            sleep(status_wait * 60)
    except:
        # Close the session
        await mazdaclient.close()

if __name__ == "__main__":
    asyncio.run(main())
