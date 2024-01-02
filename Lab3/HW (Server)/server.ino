const int WIDTH = 800;
const int HEIGHT = 800;
const int ROWS = 8;
const int COLS = 8;
const int SQUARE_SIZE = WIDTH / COLS;
const int MENU_BUTTON_WIDTH = 300;
const int MENU_BUTTON_HEIGHT = 150;

const int LIGHT[3] = {227, 193, 111};
const int DARK[3] = {184, 139, 74};

const int WHITE[3] = {255, 255, 255};
const int BLACK[3] = {0, 0, 0};
const int GREY[3] = {128, 128, 128};

const int RED[3] = {255, 0, 0};
const int GREEN[3] = {0, 255, 0};
const int BLUE[3] = {0, 0, 255};

void createConfig() {
  return "";
}

void sendConfig() {
  Serial.print(" CONFIGURATION\n");
  Serial.print("WIDTH=");
  Serial.print(WIDTH);
  Serial.print("\n");
  Serial.print("HEIGHT=");
  Serial.print(HEIGHT);
  Serial.print("\n");
  Serial.print("ROWS=");
  Serial.print(ROWS);
  Serial.print("\n");
  Serial.print("COLS=");
  Serial.print(COLS);
  Serial.print("\n");
  Serial.print("SQUARE_SIZE=");
  Serial.print(SQUARE_SIZE);
  Serial.print("\n");
  Serial.print("MENU_BUTTON_WIDTH=");
  Serial.print(MENU_BUTTON_WIDTH);
  Serial.print("\n");
  Serial.print("MENU_BUTTON_HEIGHT=");
  Serial.print(MENU_BUTTON_HEIGHT);
  Serial.print("\n");
  
  Serial.print("LIGHT=");
  Serial.print(LIGHT[0]);
  Serial.print(",");
  Serial.print(LIGHT[1]);
  Serial.print(",");
  Serial.print(LIGHT[2]);
  Serial.print("\n");

  Serial.print("DARK=");
  Serial.print(DARK[0]);
  Serial.print(",");
  Serial.print(DARK[1]);
  Serial.print(",");
  Serial.print(DARK[2]);
  Serial.print("\n");

  Serial.print("WHITE=");
  Serial.print(WHITE[0]);
  Serial.print(",");
  Serial.print(WHITE[1]);
  Serial.print(",");
  Serial.print(WHITE[2]);
  Serial.print("\n");

  Serial.print("BLACK=");
  Serial.print(BLACK[0]);
  Serial.print(",");
  Serial.print(BLACK[1]);
  Serial.print(",");
  Serial.print(BLACK[2]);
  Serial.print("\n");

  Serial.print("GREY=");
  Serial.print(GREY[0]);
  Serial.print(",");
  Serial.print(GREY[1]);
  Serial.print(",");
  Serial.print(GREY[2]);
  Serial.print("\n");

  Serial.print("RED=");
  Serial.print(RED[0]);
  Serial.print(",");
  Serial.print(RED[1]);
  Serial.print(",");
  Serial.print(RED[2]);
  Serial.print("\n");

  Serial.print("GREEN=");
  Serial.print(GREEN[0]);
  Serial.print(",");
  Serial.print(GREEN[1]);
  Serial.print(",");
  Serial.print(GREEN[2]);
  Serial.print("\n");

  Serial.print("BLUE=");
  Serial.print(BLUE[0]);
  Serial.print(",");
  Serial.print(BLUE[1]);
  Serial.print(",");
  Serial.print(BLUE[2]);
  Serial.print(";\n");
}

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(100);
}

void loop() {
  createConfig();
  sendConfig();
}