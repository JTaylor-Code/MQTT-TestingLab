
Lab 1: Setting Up the Environment
First Install Docker and Mosquitto

```bash
docker compose down
docker compose build broker
docker compose up -d broker sensor subscriber
docker compose logs -f broker
'''

Test
