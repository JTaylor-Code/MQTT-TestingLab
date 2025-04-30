FROM python:3.9
WORKDIR /app
RUN pip install paho-mqtt==1.6.1
COPY subscriber.py
CMD ["python3", "sensor.py"]
