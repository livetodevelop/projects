/*
 * Automatic Plant Waterer
 * waters plant when soil is dry
 * 
 * wiring:
 * - soil moisture sensor: A0, 5V, GND
 * - relay module (pump): pin 7
 * - optional LED indicator: pin 8
 * 
 * WARNING: dont leave water near electronics!
 */

#define MOISTURE_PIN A0
#define PUMP_PIN 7
#define LED_PIN 8

// adjust these values based on your sensor readings
const int DRY_THRESHOLD = 600;   // higher = drier soil
const int WET_THRESHOLD = 300;   // lower = wetter soil

const long WATER_INTERVAL = 5000;  // how long to run pump (ms)
const long CHECK_INTERVAL = 30000; // check every 30 seconds

unsigned long lastWaterTime = 0;
bool isWet = false;

void setup() {
  Serial.begin(9600);
  
  pinMode(PUMP_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
  
  // start with pump off
  digitalWrite(PUMP_PIN, LOW);
  digitalWrite(LED_PIN, LOW);
  
  Serial.println("Plant Waterer started");
  Serial.print("Dry threshold: ");
  Serial.println(DRY_THRESHOLD);
  Serial.print("Wet threshold: ");
  Serial.println(WET_THRESHOLD);
}

void loop() {
  unsigned long currentTime = millis();
  
  // only check periodically
  if (currentTime - lastWaterTime < CHECK_INTERVAL) {
    return;
  }
  
  lastWaterTime = currentTime;
  
  // read moisture sensor
  int moistureValue = analogRead(MOISTURE_PIN);
  
  Serial.print("Moisture reading: ");
  Serial.println(moistureValue);
  
  // determine if soil is dry (higher value = drier)
  bool needsWater = moistureValue > DRY_THRESHOLD;
  
  // hysteresis: only water if its really dry, stop when its wet enough
  if (needsWater && !isWet) {
    Serial.println("Soil is dry, watering...");
    
    // turn on pump
    digitalWrite(PUMP_PIN, HIGH);
    digitalWrite(LED_PIN, HIGH);
    
    delay(WATER_INTERVAL);
    
    // turn off pump
    digitalWrite(PUMP_PIN, LOW);
    digitalWrite(LED_PIN, LOW);
    
    isWet = true;
    Serial.println("Watering complete");
    
  } else if (moistureValue < WET_THRESHOLD) {
    // soil is wet enough
    isWet = true;
    Serial.println("Soil is wet");
    
  } else if (moistureValue > DRY_THRESHOLD + 100) {
    // still dry after watering, something might be wrong
    isWet = false;
    Serial.println("Still dry, will check again soon");
  }
  
  Serial.print("Status: ");
  Serial.println(isWet ? "wet" : "dry");
  Serial.println("---");
}
