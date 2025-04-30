import time, random
import paho.mqtt.client as mqtt
print("[SENSOR] Starting sensor...", flush=True)

BROKER = 'broker'
PORT   = 1883
TOPIC  = 'sensor/temperature'

client = mqtt.Client(client_id='sensor')
client.username_pw_set("sensor", "password")
client.connect(BROKER, PORT)       

while True:
  temp = round(20 + random.random()*10, 2)
  client.publish(TOPIC, temp)
  print(f"[SENSOR] Published: {temp}", flush=True)
  time.sleep(5)

