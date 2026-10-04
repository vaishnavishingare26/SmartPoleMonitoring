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

        🔧 Hardware Components
Component	Purpose
ESP32	Main IoT controller
INA219	Current measurement
Relay Module	Automatic power cutoff
DC-DC Buck Converter	Voltage regulation
LED / Pole Load	Monitored electrical load
5V Power Supply	System power


🔌 Hardware Connections
Pin numbers should match the actual hardware implementation.

Component	ESP32 Connection	Purpose
INA219 SDA	GPIO 21	I2C Data
INA219 SCL	GPIO 22	I2C Clock
Relay Module	Project-defined GPIO	Automatic power cutoff
Power Supply	VIN / regulated input	System power


🚨 Fault Detection
The system continuously monitors the current drawn by the
connected electrical load.
When the measured current exceeds the configured threshold,
the system identifies an abnormal condition and can activate
the relay-based power cutoff mechanism.
☁️ Cloud Monitoring
ThingSpeak is used for remote monitoring and visualization of
sensor data.
The system can publish parameters such as:
- Pole status
- Current measurements
- Fault status
- Power-cut status
💻 Software Stack
Embedded / IoT
- ESP32
- Arduino
- INA219
- Relay Module
- ThingSpeak
Programming
- Python
- C/C++
- HTML
- CSS
- JavaScript
Libraries / Technologies
- OpenCV
- Requests
- PyWhatKit
- ThingSpeak API
📂 Project Structure
SmartPoleMonitoring/
│
├── assets/
├── modules/
├── pole.ino/
├── templates/
├── web_dashboard/
│
├── LiveImageCapturter.py
├── MainGUI.py
├── Monitoring_Engine.py
├── PowerCutModule.py
├── WhatsAppSender.py
├── dashboard.py
├── dashboard.html
├── live_camera.py
├── live_stream.py
├── location_fetch.py
├── login_gui.py
├── main.py
├── prevention_logs.html
├── .gitignore
└── README.md

🚀 Getting Started
Clone the Repository
git clone https://github.com/vaishnavishingare26/SmartPoleMonitoring.git
cd SmartPoleMonitoring

Install Python Dependencies
pip install -r requirements.txt

Run the Monitoring System
python main.py

Configure the ESP32, sensor, ThingSpeak credentials and other
required settings before running the complete system.

🔮 Future Scope
- Multi-pole centralized monitoring
- Mobile application integration
- Advanced fault classification
- Predictive maintenance using Machine Learning
- Cloud-based analytics
- Automated maintenance alerts
👩‍💻 Author
Vaishnavi Shingare
Computer Engineering Student
Interested in IoT, Machine Learning, Data Science and Software Development.
