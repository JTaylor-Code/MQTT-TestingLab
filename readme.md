## Lab 1: Setting Up the Environment
First install Docker and Mosquitto.
Running this script will install Docker.
```bash
#!/bin/bash
# Update and install dependencies
sudo apt update
sudo apt install -y ca-certificates curl gnupg lsb-release

# Add Docker GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Add Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update and install Docker Engine and Compose plugin
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Add current user to docker group to avoid using sudo for docker commands
sudo usermod -aG docker $USER

# Test installation (may require logout/login to take effect)
newgrp docker << END
docker --version
docker compose version
END
```
After this, we should reboot the virtual machine. Now we can install Mosquitto
```bash
sudo apt update
sudo apt install -y mosquitto-clients mosquitto
```
Then run the following to make sure that the environment works.
```bash
docker compose up --build broker sensor subscriber
```

## Lab 2: Brute-Foce Password Attack
We have already set up the lab in such a way that passwords are required (this can be changed in the configuration file by setting allow_anonymous to true). To create specifc passwords for both the sensor and subscriber, we will want to run the following within the broker directory from the command line.
```bash
cd broker
mosquitto_passwd -c password.txt sensor
# → enter: password
mosquitto_passwd password.txt subscriber
# → enter: password
cd ..
```
Next, we need to run docker compose down and re-spin up the network.
```bash
docker compose up --build attacker-bruteforce
```
The output for this should show that the password "password" results in a successful connection with subscriber and sensor.

## Lab 3: Injection Attack
Once again we run:
```bash
docker compose down
```
Which will reset our docker containers, then we restart them again with:
```bash
docker compose up -d broker subscriber sensor
```
We should also monitor the subscriber logs:
```bash
docker compose logs -f subsriber
```
Running our attacker's script in a separate window, but the same directory:
```bash
docker compose up --build attacker-injection
```
We should then see in the subscriber logs the messages that we injected using our attacker's script. This will be easiest if both terminal windows are side-by-side.

## Lab 4: DoS Attack
Lastly, we can run the script:
```bash
docker compose up --build attacker-dos
```
And monitoring the logs of the subscriber, we can see that there is a flood of FAKE_TEMP readings which simulate a DoS attack.

## Lab 5: Packet Sniffing
This lab assumes that wireshark is already installed. First the user should run wireshark in root access. We should first reset the machines by using:
```bash
docker compose down
```
And then restarting our containers:
```bash
docker compose up -d broker subscriber sensor
```
Then select the correct interface on wireshark, it may start with "br".
Filtering out for the MQTT packets, we can easily decode the message within the detail pane from hex to something readable using a decoder like Cyberchef.
Next we want to run the attack-injection docker again so that we can see what happens with a connect initiation. Filtering out using
```bash
mqtt.msgtype==1
```
We can see that the connect command clearly states the password in clear-text.


