int redPin = 7;
int greenPin = 6;
int bluePin = 5;
int moodChar = 0; // 0 would be happy by default

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    moodChar = Serial.read();
    // TODO: add logic to translate to different colors after inputting the moodChar so that the code feels complete
    // TODO: give users the freedom to choose the color of their choice 
  }
}

void setColor(int redValue, int greenValue, int blueValue) {
  analogWrite(redPin, redValue);
  analogWrite(greenPin, greenValue);
  analogWrite(bluePin, blueValue);
}

void translateToColor(int startRedValue, int startGreenValue, int startBlueValue, int endRedValue, int endGreenValue, int endBlueValue) {
  for (int i = startRedValue; i <= endRedValue; i++) {
    for (int j = startGreenValue; j <= endGreenValue; j++) {
      for (int k = startBlueValue; k <= endBlueValue; k++) {
        setColor(i, j, k);
      }
    }
  }
}