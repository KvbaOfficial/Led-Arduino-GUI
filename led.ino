const int redPin = 9;    // Red led pin
const int greenPin = 10; // Green led pin
const int bluePin = 11;  // Blue led pin

void setup() {
  Serial.begin(115200);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String received = Serial.readStringUntil('\n');
    int commaIndex1 = received.indexOf(',');
    int commaIndex2 = received.lastIndexOf(',');

    int red = received.substring(0, commaIndex1).toInt();
    int green = received.substring(commaIndex1 + 1, commaIndex2).toInt();
    int blue = received.substring(commaIndex2 + 1).toInt();

    setColor(red, green, blue);
  }
}

void setColor(int red, int green, int blue) {
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}