  
int analogPin = 3;     
int data = 0;           
char userInput;

void setup(){

  Serial.begin(9600);                        //  setup serial

}

void loop(){

if(Serial.available()> 0){ 
    
    userInput = Serial.read();               // read user input
      
      if(userInput == 'g'){                  // if we get expected value 

            data = analogRead(analogPin);    // read the input pin
            Serial.println(data);            
            
      } // if user input 'g' 
  } // Serial.available
} // Void Loop




