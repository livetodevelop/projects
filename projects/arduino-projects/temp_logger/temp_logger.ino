/*
 * Temperature Logger
 * logs temp/humidity to SD card every minute
 * displays on OLED screen
 * 
 * wiring:
 * - DHT11: pin 4, 5V, GND
 * - OLED (I2C): SDA/A4, SCL/A5, VCC, GND
 * - SD Card module: SPI pins + 10 for CS
 */

#include <DHT.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <SPI.h>
#include <SD.h>

#define DHT_PIN 4
#define DHT_TYPE DHT11
#define SD_CS 10
#define OLED_RESET 4

DHT dht(DHT_PIN, DHT_TYPE);
Adafruit_SSD1306 display(128, 64, &Wire, OLED_RESET);

File dataFile;

const long LOG_INTERVAL = 60000;  // 1 minute
unsigned long lastLogTime = 0;

void setup() {
  Serial.begin(9600);
  
  dht.begin();
  
  // init OLED
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("OLED failed");
    return;
  }
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println("Temp Logger");
  display.display();
  
  // init SD card
  if (!SD.begin(SD_CS)) {
    display.println("SD card failed!");
    display.display();
    Serial.println("SD card initialization failed");
    return;
  }
  display.println("SD card OK");
  display.display();
  
  // create/open log file
  dataFile = SD.open("templog.csv", FILE_WRITE);
  if (!dataFile) {
    display.println("Could not open log file");
    display.display();
    return;
  }
  
  // write header if file is new
  if (dataFile.size() == 0) {
    dataFile.println("timestamp,temp_c,humidity%");
  }
  dataFile.close();
  
  delay(2000);
  display.clearDisplay();
  display.display();
}

void loop() {
  unsigned long currentTime = millis();
  
  // read sensor
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor");
    display.clearDisplay();
    display.setCursor(0, 0);
    display.println("Sensor error");
    display.display();
    return;
  }
  
  // display current readings
  display.clearDisplay();
  display.setCursor(0, 0);
  display.print("Temp: ");
  display.print(temperature);
  display.println(" C");
  display.print("Humid: ");
  display.print(humidity);
  display.println(" %");
  
  // show next log time
  unsigned long timeUntilLog = LOG_INTERVAL - (currentTime % LOG_INTERVAL);
  display.setCursor(0, 40);
  display.print("Next log: ");
  display.print(timeUntilLog / 1000);
  display.println("s");
  
  display.display();
  
  // log to SD card
  if (currentTime - lastLogTime >= LOG_INTERVAL) {
    logToSD(temperature, humidity);
    lastLogTime = currentTime;
    
    // blink LED to show logging happened
    digitalWrite(13, HIGH);
    delay(100);
    digitalWrite(13, LOW);
  }
  
  delay(1000);
}

void logToSD(float temp, float humid) {
  dataFile = SD.open("templog.csv", FILE_WRITE);
  
  if (dataFile) {
    dataFile.print(millis());
    dataFile.print(",");
    dataFile.print(temp);
    dataFile.print(",");
    dataFile.println(humid);
    dataFile.close();
    
    Serial.print("Logged: ");
    Serial.print(temp);
    Serial.print("C, ");
    Serial.println(humid);
  } else {
    Serial.println("Error opening log file");
  }
}
