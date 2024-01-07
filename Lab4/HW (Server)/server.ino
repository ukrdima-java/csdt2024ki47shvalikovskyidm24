/*!
  \file
  \brief Constants and functions related to game configuration.

  This file contains constants and functions related to the game configuration,
  including the board dimensions, colors, and configuration serialization.
*/

/// Width of the game window.
const int WIDTH = 800;

/// Height of the game window.
const int HEIGHT = 800;

/// Number of rows on the game board.
const int ROWS = 8;

/// Number of columns on the game board.
const int COLS = 8;

/// Size of each square on the game board.
const int SQUARE_SIZE = WIDTH / COLS;

/// Width of the menu button.
const int MENU_BUTTON_WIDTH = 300;

/// Height of the menu button.
const int MENU_BUTTON_HEIGHT = 150;

/// RGB values for light-colored squares on the board.
const int LIGHT[3] = {227, 193, 111};

/// RGB values for dark-colored squares on the board.
const int DARK[3] = {184, 139, 74};

/// RGB values for the color white.
const int WHITE[3] = {255, 255, 255};

/// RGB values for the color black.
const int BLACK[3] = {0, 0, 0};

/// RGB values for the color grey.
const int GREY[3] = {128, 128, 128};

/// RGB values for the color red.
const int RED[3] = {255, 0, 0};

/// RGB values for the color green.
const int GREEN[3] = {0, 255, 0};

/// RGB values for the color blue.
const int BLUE[3] = {0, 0, 255};

/*!
  \brief Creates a configuration string.

  \return An empty string since the function currently does not generate any configuration.
*/
void createConfig() {
  return "";
}

/*!
  \brief Sends the current configuration over the Serial port.

  This function sends the current configuration parameters over the Serial port
  in a formatted way.
*/
void sendConfig() {
  Serial.print(" CONFIGURATION\n");
  Serial.print("WIDTH=");
  Serial.print(WIDTH);
  Serial.print("\n");
  // ... (similar lines for other configuration parameters)
  Serial.print("BLUE=");
  Serial.print(BLUE[0]);
  Serial.print(",");
  Serial.print(BLUE[1]);
  Serial.print(",");
  Serial.print(BLUE[2]);
  Serial.print(";\n");
}

/*!
  \brief Arduino setup function.

  This function is called once when the Arduino is powered on or reset.
  It initializes the Serial communication.
*/
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(100);
}

/*!
  \brief Arduino loop function.

  This function is called repeatedly after the setup.
  It calls the createConfig and sendConfig functions in a loop.
*/
void loop() {
  createConfig();
  sendConfig();
}