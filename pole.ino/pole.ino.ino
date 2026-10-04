#include <WiFi.h>
#include <Wire.h>
#include <HTTPClient.h>
#include <Adafruit_INA219.h>

Adafruit_INA219 ina219;

// WiFi credentials
const char* ssid = "vivo Y27";
const char* password = "vaishu_2624";

// ThingSpeak Write API
String apiKey = "B87MF5U7V14N4NGH";

// ThingSpeak server
const char* server = "https://api.thingspeak.com/update";

float current_mA = 0;

int pole1_status = 0;
int pole2_status = 0;

void connectWiFi()
{
  Serial.print("Connecting WiFi");

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi Connected");
}

void setup()
{
  Serial.begin(115200);

  Wire.begin();

  if (!ina219.begin())
  {
    Serial.println("INA219 not detected");
    while (1);
  }

  Serial.println("INA219 Sensor Ready");

  connectWiFi();
}

void loop()
{

  // ---- Read current ----
  current_mA = ina219.getCurrent_mA();

  Serial.print("Current: ");
  Serial.print(current_mA);
  Serial.println(" mA");

  // ---- Pole1 Detection ----
  if (current_mA > 0.70)     // threshold
  {
    pole1_status = 1;
  }
  else
  {
    pole1_status = 0;
  }

  // Pole2 default
  pole2_status = 0;

  Serial.print("Pole1 Status: ");
  Serial.println(pole1_status);

  Serial.print("Pole2 Status: ");
  Serial.println(pole2_status);

  // ---- Send Data to ThingSpeak ----
  if (WiFi.status() != WL_CONNECTED)
  {
    connectWiFi();
  }

  HTTPClient http;

  String url = String(server) + "?api_key=" + apiKey +
               "&field1=" + String(pole1_status) +
               "&field2=" + String(pole2_status);

  http.begin(url);

  int httpCode = http.GET();

  if (httpCode > 0)
  {
    Serial.println("Data Sent to ThingSpeak");
  }
  else
  {
    Serial.println("Error sending data");
  }

  http.end();

  Serial.println("-----------------------");

  delay(1000);   // ThingSpeak minimum delay
}