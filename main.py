import time
import ubinascii
from umqtt.simple import MQTTClient
import machine
import random
import config


client_id = ubinascii.hexlify(machine.unique_id())
subscribe_topic = b"to_device/#"


def sub_cb(topic, msg):
    print((topic, msg))


def reset():
    print("Resetting...")
    time.sleep(5)
    machine.reset()
    
    
def main():
    print(f"Begin connection with MQTT Broker :: {config.mqtt["broker"]}")
    mqtt_client = MQTTClient(
        client_id,
        config.mqtt["broker"],
    )
    mqtt_client.set_callback(sub_cb)
    mqtt_client.connect()
    mqtt_client.subscribe(subscribe_topic)
    print(f"Connected to MQTT  Broker :: {config.mqtt["broker"]}, and waiting for callback function to be called!")
    while True:
        mqtt_client.check_msg()
        time.sleep(1)


if __name__ == "__main__":
    while True:
        try:
            main()
        except OSError as e:
            print("Error: " + str(e))
            reset()