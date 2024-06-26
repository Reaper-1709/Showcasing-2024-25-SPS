#define redPin 7
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

int moodChar = MOOD_NEUTRAL; // Default mood

void setup() {
  // Basic arduino setup
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {

    // Parse data (Example: 1,1,50,60,50) (The value for customColorMoodChar would be left 7 if there is no customization provided by user)
    int moodCharVal = Serial.readStringUntil(',').toInt();
    int customColorMoodCharVal = Serial.readStringUntil(',').toInt();
    int redVal = Serial.readStringUntil(',').toInt();
    int greenVal = Serial.readStringUntil(',').toInt();
    int blueVal = Serial.readStringUntil(':').toInt();

    // Set color based on customization flag
    setColorFromInput(moodCharVal, customColorMoodCharVal, redVal, greenVal, blueVal);
  }
}

// Function to set color based on user input
void setColorFromInput(int moodChar, int customColorMoodChar, int red, int green, int blue) {
  int* palette = getMoodPalette(moodChar); // Get default palette

  // Apply custom color if mood matches custom mood character
  if (moodChar == customColorMoodChar) {
    palette[3] = red; // The new red value defined by user
    palette[4] = green; // The new green value defined by user
    palette[5] = blue; // The new blue value defined by user
  }

  // Set the color using the generated palette
  translateToColor(palette[0], palette[1], palette[2], palette[3], palette[4], palette[5]);
  delete[] palette; // Deallocate memory after use
}

// Function to retrieve palette based on mood character
int* getMoodPalette(int moodChar) {
  static int palette[6]; // Pre-allocate memory for palette (static for efficiency)

  switch (moodChar) { // To get the required composition
    case MOOD_ANGRY: // Angry (Red)
      palette[0] = 255; // Red
      palette[1] = 0;   // Dark Red
      palette[2] = 0;   // Dark Red
      palette[3] = 255; // Red
      palette[4] = 50;  // Light Coral
      palette[5] = 50;  // Light Coral
      break;
    case MOOD_DISGUST: // Disgust (Greenish-Yellow)
      palette[0] = 150; // Lime Green
      palette[1] = 200; // Chartreuse
      palette[2] = 0;   // Dark Olive Green
      palette[3] = 200; // Chartreuse
      palette[4] = 255; // Yellow
      palette[5] = 50;  // Light Yellow
      break;
    case MOOD_FEAR: // Fear (Blue)
      palette[0] = 0;   // Midnight Blue
      palette[1] = 0;   // Midnight Blue
      palette[2] = 100; // Royal Blue
      palette[3] = 50;  // Dark Slate Blue
      palette[4] = 50;  // Dark Slate Blue
      palette[5] = 255; // Sky Blue
      break;
    case MOOD_HAPPY: // Happy (Yellow)
      palette[0] = 255; // Yellow
      palette[1] = 200; // Gold
      palette[2] = 0;   // Dark Orange
      palette[3] = 255; // Yellow
      palette[4] = 255; // White
      palette[5] = 50;  // Light Yellow
      break;
    case MOOD_SAD: // Sad (Blue-ish)
      palette[0] = 0;   // Midnight Blue
      palette[1] = 50;  // Dark Slate Blue
      palette[2] = 100; // Royal Blue
      palette[3] = 50;  // Dark Slate Blue
      palette[4] = 150; // Medium Slate Blue
      palette[5] = 255; // Sky Blue
      break;
    case MOOD_SURPRISE: // Surprise (White with a Flash)
      palette[0] = 255; // White
      palette[1] = 255; // White
      palette[2] = 255; // White
      palette[3] = 100; // Light Gray
      palette[4] = 100; // Light Gray
      palette[5] = 100; // Light Gray
      break;
    case MOOD_NEUTRAL: // Neutral (Soft White)
      palette[0] = 150; // Light Gray
      palette[1] = 150; // Light Gray
      palette[2] = 150; // Light Gray
      palette[3] = 200; // Silver
      palette[4] = 200; // Silver
      palette[5] = 200; // Silver
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
void translateToColor(int startRed, int startGreen, intStartBlue, int endRed, int endGreen, int endBlue) {
  int steps = 20; // Adjust steps for desired transition effect
  int redDiff = (endRed - startRed) / steps;
  int greenDiff = (endGreen - startGreen) / steps;
  int blueDiff = (endBlue - startBlue) / steps;

  for (int i = 0; i <= steps; i++) {
    int currentRed = startRed + (i * redDiff);
    int currentGreen = startGreen + (i * greenDiff);
    int currentBlue = startBlue + (i * blueDiff);
    setColor(currentRed, currentGreen, currentBlue);
    delay(10);  // Adjust delay for desired transition speed
  }
}

// Function to set color to pins
void setColor(int redValue, int greenValue, int blueValue) {
  analogWrite(redPin, redValue);
  analogWrite(greenPin, greenValue);
  analogWrite(bluePin, blueValue);
}
