#define BLYNK_TEMPLATE_ID "YourTemplateID"
#define BLYNK_DEVICE_NAME "YourDeviceName"
#define BLYNK_AUTH_TOKEN "YourAuthToken"

#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

char ssid[] = "YourWiFiSSID";
char pass[] = "YourWiFiPassword";

int ledPin = D1; // Pin where LED is connected

void setup() {
  pinMode(ledPin, OUTPUT);
  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);
}

void loop() {
  Blynk.run();
}

// Blynk Virtual Pin V0 (On/Off Button)
BLYNK_WRITE(V0) {
  int pinValue = param.asInt(); // Get value from app (1 or 0)
  digitalWrite(ledPin, pinValue); // Set LED state
}