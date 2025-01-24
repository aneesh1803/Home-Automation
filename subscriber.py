import paho.mqtt.client as mqtt

# MQTT Broker details
broker = "test.mosquitto.org"
port = 1883
topic = "home/automation"

# Handle incoming messages
def on_message(client, userdata, message):
    command = message.payload.decode()
    if command == "light_on":
        print("Light turned ON")
    elif command == "light_off":
        print("Light turned OFF")
    elif command == "fan_on":
        print("Fan turned ON")
    elif command == "fan_off":
        print("Fan turned OFF")
    else:
        print("Unknown command received")

# MQTT Subscriber setup
def setup_subscriber():
    client = mqtt.Client()
    client.connect(broker, port)
    client.subscribe(topic)
    client.on_message = on_message
    print("Listening for commands...")
    client.loop_forever()

# Example usage
if __name__ == "__main__":
    setup_subscriber()
