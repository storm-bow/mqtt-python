from paho.mqtt import client as mqtt_client
import random
import time
import json

broker = 'broker.emqx.io'
port = 1883
topic = "Bow-Chat"
client_id = ""
# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f"Connected to bow-chat as {client_id}")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = input("")
        #msg = f"#{client_id}: {msg}"
        msg = {
            "message": msg,
            "user": client_id
        }
        msg = json.dumps(msg)
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status != 0:
            print(f"error")


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        msg = msg.payload.decode()
        msg = json.loads(msg)
        if(msg["user"] != client_id):
            print("#"+msg["user"]+": "+msg["message"])
        

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    client.loop_start()
    subscribe(client)
    publish(client)


if __name__ == '__main__':
    client_id = input("Set username:")
    run()