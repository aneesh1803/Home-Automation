import paho.mqtt.client as mqtt

# MQTT Broker details
broker = "test.mosquitto.org"
port = 1883
topic = "home/automation"

# Publish commands
def publish_command(command):
    client = mqtt.Client()
    client.connect(broker, port)
    client.publish(topic, command)
    print(f"Command sent: {command}")
    client.disconnect()

# Example usage
if __name__ == "__main__":
    print("Home Automation Control Panel")
    print("1. Turn on light")
    print("2. Turn off light")
    print("3. Turn on fan")
    print("4. Turn off fan")

    choice = input("Enter your choice: ")
    commands = {
        "1": "light_on",
        "2": "light_off",
        "3": "fan_on",
        "4": "fan_off"
    }
    command = commands.get(choice, "Invalid command")
    if command != "Invalid command":
        publish_command(command)
    else:
        print("Invalid choice")
