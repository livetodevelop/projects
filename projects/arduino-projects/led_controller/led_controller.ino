/*
 * LED Strip Controller with Potentiometer
 * controls WS2812B LED strip
 * 
 * wiring:
 * - potentiometer: A0, 5V, GND
 * - button: pin 2, GND (with internal pullup)
 * - LED strip data: pin 6
 */

#include <Adafruit_NeoPixel.h>

#define PIN 6
#define NUM_PIXELS 30
#define POT_PIN A0
#define BUTTON_PIN 2

Adafruit_NeoPixel strip(NUM_PIXELS, PIN, NEO_GRB + NEO_KHZ800);

bool partyMode = false;
unsigned long lastButtonPress = 0;
const long DEBOUNCE_DELAY = 200;

void setup() {
  strip.begin();
  strip.show();
  strip.setBrightness(100);
  
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  
  // set all LEDs to white initially
  colorWipe(strip.Color(50, 50, 50), 50);
}

void loop() {
  // check button for party mode
  if (digitalRead(BUTTON_PIN) == LOW) {
    unsigned long currentTime = millis();
    
    if (currentTime - lastButtonPress > DEBOUNCE_DELAY) {
      partyMode = !partyMode;
      lastButtonPress = currentTime;
      
      if (!partyMode) {
        // turn off party mode, back to normal
        strip.clear();
      }
    }
    delay(50);
  }
  
  if (partyMode) {
    runPartyMode();
  } else {
    // read potentiometer and set color
    int potValue = analogRead(POT_PIN);
    
    // map pot value (0-1023) to hue (0-65535)
    uint16_t hue = map(potValue, 0, 1023, 0, 65535);
    
    // convert HSV to RGB (simplified)
    uint32_t color = Wheel(hue);
    
    for (int i = 0; i < strip.numPixels(); i++) {
      strip.setPixelColor(i, color);
    }
    strip.show();
  }
  
  delay(10);
}

void runPartyMode() {
  static uint16_t currentHue = 0;
  
  currentHue += 50;  // change speed
  
  uint32_t color = Wheel(currentHue);
  
  for (int i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, color);
  }
  strip.show();
  
  delay(30);
}

// input a value 0-65535 to get a color from the rainbow
uint32_t Wheel(uint16_t WheelPos) {
  if (WheelPos < 21845) {
    return strip.Color(255, WheelPos * 3 / 256, 0);
  } else if (WheelPos < 43690) {
    return strip.Color(255 - ((WheelPos - 21845) * 3 / 256), 255, 0);
  } else {
    return strip.Color(0, 255 - ((WheelPos - 43690) * 3 / 256), (WheelPos - 43690) * 3 / 256);
  }
}

// fill pixels one after another with a color
void colorWipe(uint32_t color, int wait) {
  for (int i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, color);
    strip.show();
    delay(wait);
  }
}
