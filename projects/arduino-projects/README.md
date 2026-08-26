# Arduino Projects

random arduino stuff i've been making. nothing too fancy but they work most of the time

## projects

### LED Strip Controller (`led_controller/`)
- controls WS2812B LED strip with potentiometer
- change colors by turning knob
- has a "party mode" button that cycles through colors
- code is kinda messy but it works

### Temperature Logger (`temp_logger/`)
- logs room temperature every minute to SD card
- uses DHT11 sensor
- displays current temp on OLED screen
- battery powered so i can move it around

### Auto Plant Waterer (`plant_waterer/`)
- waters my plants when soil is dry
- uses soil moisture sensor + small pump
- runs off a 9V battery
- killed one plant already because i overwatered it oops

## requirements

depends on the project but generally:
- Arduino IDE
- various libraries (see individual folders)
- patience because arduino code is annoying to debug

## uploading

1. open `.ino` file in Arduino IDE
2. select your board (i use Nano mostly)
3. click upload
4. pray it works

## notes

- all these were made with parts from ebay so quality varies
- some circuits are probably not safe but nothing has caught fire yet
- would recommend actually testing before leaving stuff running unattended lol
