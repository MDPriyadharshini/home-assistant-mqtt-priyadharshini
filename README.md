# Home Assistant MQTT Assignment – Nakshatra Automation

## Student Details
- **Name:** Priyadharshini M D
- **Register Number:** 42111019
- **MQTT Topic:** `home/priyadharshini-2025/sensor`

## Project Overview
This project demonstrates integration between a Python script, an MQTT broker (Mosquitto), and Home Assistant.

The Python script publishes three sensor values to an MQTT topic:

- `temperature` = 25 °C  
- `humidity` = 60 %  
- `light` = 300 lx (extra sensor: Light Intensity)

These values are then consumed by Home Assistant via the MQTT integration and displayed on the dashboard.

## Components Used
- **Home Assistant** (Docker container)
- **Mosquitto MQTT Broker** (running on Windows)
- **Python 3** with `paho-mqtt` library

## How It Works

1. Mosquitto is started with a configuration that listens on port **1883** and allows local connections.
2. Home Assistant connects to the MQTT broker using:
   - Broker: `host.docker.internal`
   - Port: `1883`
3. The Python script connects to the same broker at `localhost:1883` and publishes JSON data to:
   - Topic: `home/priyadharshini-2025/sensor`
4. Home Assistant defines three MQTT sensors that read `temperature`, `humidity`, and `light` from the JSON payload and displays them on the dashboard.

## Python Script

The main script is `mqtt_publish.py`. It contains the required variables:

```python
student_name = "Priyadharshini M D"
unique_id = "42111019"
topic = "home/priyadharshini-2025/sensor"
