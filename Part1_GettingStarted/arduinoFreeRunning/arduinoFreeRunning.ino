  
int analogPin = 3;     
int data = 0; 
char userInput;          

void setup(){

  Serial.begin(9600);          //  setup serial

}

void loop(){


      data = analogRead(analogPin);    // read the input pin
      Serial.println(data);            // print the data to the serial bus

} // Void Loop




