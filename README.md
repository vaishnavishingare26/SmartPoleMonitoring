# ⚡ Smart Pole Monitoring System

### IoT-Based Electrical Pole Monitoring & Short-Circuit Detection

Smart Pole Monitoring is an IoT-based system designed to monitor
electrical pole loads in real time and detect abnormal current
conditions.

The system uses an ESP32, INA219 current sensor, relay-based
automatic power cutoff, and ThingSpeak for remote monitoring.

---

## ✨ Key Features

- ⚡ Real-time electrical current monitoring
- 🔍 Short-circuit / abnormal-current detection
- 🚨 Automatic power cutoff using relay
- ☁️ ThingSpeak-based remote monitoring
- 📊 Live monitoring dashboard
- 📷 Live image capture
- 📱 Alert/notification support
- 🖥️ Python-based monitoring engine
- 🔌 ESP32-based hardware control

---

## 🏗️ System Architecture

```text
Electrical Pole / Load
        │
        ▼
    INA219 Sensor
        │
        ▼
      ESP32
        │
        ├──────────► Relay / Power Cutoff
        │
        ▼
    ThingSpeak
        │
        ▼
Monitoring Engine
        │
        ├────────► Dashboard
        ├────────► Image Capture
        └────────► Alerts / Notifications
