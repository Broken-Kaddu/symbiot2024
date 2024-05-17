
const int buzzerPin = 9;
String command = "";

void setup() {
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    command = Serial.readStringUntil('\n');
    command.trim(); 

    if (command == "ON") {
      tone(buzzerPin, 5000); 
    } else if (command == "OFF") {
      noTone(buzzerPin); 
    }
  }
}

