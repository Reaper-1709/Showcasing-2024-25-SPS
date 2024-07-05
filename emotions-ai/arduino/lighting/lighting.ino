#define redPin 9
#define greenPin 6
#define bluePin 5

// Mood characters (assuming these values represent different moods (They are taken from FER-2013 website))
#define MOOD_ANGRY 0
#define MOOD_DISGUST 1
#define MOOD_FEAR 2
#define MOOD_HAPPY 3
#define MOOD_SAD 4
#define MOOD_SURPRISE 5
#define MOOD_NEUTRAL 6

void setup() {
  
  // Basic arduino setup
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    // Parse data (Example: 1:)
    int moodCharVal = Serial.readStringUntil(':').toInt();
    setColorFromInput(moodCharVal);
  }
}

// Function to set color based on user input
void setColorFromInput(int moodChar) {
   // Get default palette
    int* palette = getMoodPalette(moodChar);
    translateToColor(palette[0], palette[1], palette[2], palette[3], palette[4], palette[5]);
}

// Function to retrieve palette based on mood character
int * getMoodPalette(int moodChar) {
  static int palette[6]; // Pre-allocate memory for palette (static for efficiency)

  switch (moodChar) { // To get the required composition
    case MOOD_ANGRY: // Angry (Red)
      palette[0] = 254; // Red
      palette[1] = 0;   // Dark Red
      palette[2] = 0;   // Dark Red
      palette[3] = 254; // Red
      palette[4] = 0;  // Light Coral
      palette[5] = 0;  // Light Coral
      break;
    case MOOD_DISGUST: // Disgust (Greenish-Yellow)
      palette[0] = 150; // Lime Green
      palette[1] = 200; // Chartreuse
      palette[2] = 0;   // Dark Olive Green
      palette[3] = 200; // Chartreuse
      palette[4] = 254; // Yellow
      palette[5] = 50;  // Light Yellow
      break;
    case MOOD_FEAR: // Fear (Blue)
      palette[0] = 0;   // Midnight Blue
      palette[1] = 0;   // Midnight Blue
      palette[2] = 100; // Royal Blue
      palette[3] = 0;  // Dark Slate Blue
      palette[4] = 0;  // Dark Slate Blue
      palette[5] = 255; // Sky Blue
      break;
    case MOOD_HAPPY: // Happy (Yellow)
      palette[0] = 0; // Yellow
      palette[1] = 0; // Gold
      palette[2] = 0;   // Dark Orange
      palette[3] = 225; // Yellow
      palette[4] = 255; // White
      palette[5] = 0;  // Light Yellow
      break;
    case MOOD_SAD: // Sad (Blue-ish)
      palette[0] = 0;   // Midnight Blue
      palette[1] = 50;  // Dark Slate Blue
      palette[2] = 100; // Royal Blue
      palette[3] = 50;  // Dark Slate Blue
      palette[4] = 150; // Medium Slate Blue
      palette[5] = 254; // Sky Blue
      break;
    case MOOD_SURPRISE: // Surprise (White with a Flash)
      palette[0] = 0; // White
      palette[1] = 0; // White
      palette[2] = 0; // White
      palette[3] = 100; // Light Gray
      palette[4] = 100; // Light Gray
      palette[5] = 100; // Light Gray
      break;
    case MOOD_NEUTRAL: // Neutral (Soft White)
      palette[0] = 0; // Light Gray
      palette[1] = 0; // Light Gray
      palette[2] = 0; // Light Gray
      palette[3] = 100; // Silver
      palette[4] = 0; // Silver
      palette[5] = 255; // Silver
      break;
    default: // Anything else (black / turn off)
      palette[0] = 0;
      palette[1] = 0;
      palette[2] = 0;
      palette[3] = 0;
      palette[4] = 0;
      palette[5] = 0;
  }

  return palette; // Return pointer to the pre-allocated palette
}

// Function for color transition
void translateToColor(int startRed, int startGreen, int startBlue, int endRed, int endGreen, int endBlue) {
  setColor(endRed, endGreen, endBlue);
}

// Function to set color to pins
void setColor(int redValue, int greenValue, int blueValue) {
  analogWrite(redPin, redValue);
  analogWrite(greenPin, greenValue);
  analogWrite(bluePin, blueValue);
}
