import paho.mqtt.client as mqtt
print("[SUBSCRIBER] Starting subscriber...", flush=True)

BROKER = 'broker'
PORT   = 1883
TOPIC  = 'sensor/temperature'


client = mqtt.Client(client_id='subscriber')
client.username_pw_set("subscriber", "password")
def on_connect(client, userdata, flags, rc):
  print("[SUBSCRIBER] Connected with result code " + str(rc))
  client.subscribe(TOPIC)

def on_message(client, userdata, msg):
  print(f"[SUBSCRIBER] Received: {msg.payload.decode()}", flush=True)


client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)     
client.loop_forever()

