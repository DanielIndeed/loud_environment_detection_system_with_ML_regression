const int microphonePin = A0; //microphone pin

void setup() {
Serial.begin(9600); //
}

void loop() {
  int s=0;
  for (int j=0; j<5; ++j){
    int mn = 512;
    int mx = 0;
    for (int i = 0; i < 1000; ++i) { //getting the values will take 1 second so that its as precise as possible
      int value = analogRead(microphonePin); //command needed to read the value from the microphone
      mn = min(mn, value);
      mx = max(mx, value);
      delay(1);     
    } //calculates the minimum and the maximum, within the time limit set by the variable i, regarding the values read by the microphone
    int volume = mx-mn;
    int db = map(volume,20,900,50,140); //this is the command that we used to get the decibel measurement
    s=s+db;
    }
  Serial.println(s/5);
  delay(500); //delay bewteen each test, set to 0.5 seconds so the AI can have a   constant flux of information
}
//the code is not long, but that's what we wanted to make the project as efficient as possible.


