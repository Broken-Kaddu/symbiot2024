const int buzzer = 9;
String command = "";

void setup() {
 
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
}


void loop() {
  

  if (Serial.available() > 0) {
    command = Serial.readStringUntil('\n');
    command.trim(); 

    if (command == "ON") {
      
      digitalWrite(buzzer,HIGH);

}
} else if (command == "OFF") {
      noTone(buzzer); 
    }
  }


