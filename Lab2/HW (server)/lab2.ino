void setup() {
  Serial.begin(9600);
  Serial.setTimeout(100);
}

void loop() {
  String receivedData = "";
  String additionalData = " Shvalikovskyi";
  String terminator = ";";

  while(true) {
    if (Serial.available() > 0) {
      receivedData += Serial.readString();
      if (receivedData.indexOf(";") > 0) break;
    }
  }

  if (receivedData.indexOf(";") > 0) {
    receivedData.replace(";", "");
    receivedData.replace("\n", "");
    receivedData = receivedData + additionalData + terminator;

    Serial.println(receivedData);
  }
}