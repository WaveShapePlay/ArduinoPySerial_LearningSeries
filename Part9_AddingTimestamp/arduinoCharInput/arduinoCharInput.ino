  
int analogPin = 3;     
int data = 0;           
char userInput;
unsigned long currentTime = 0;
unsigned long previousTime = 0;

void setup(){

  Serial.begin(9600);            //  setup serial

}

void loop(){

if(Serial.available()> 0){ 
    
    userInput = Serial.read();               // read user input
      
      if(userInput == 'g'){                  // if we get expected value 
            data = analogRead(analogPin);    // read the input pin
            Serial.println(data);   
                     
      } // if user input 'g'

      if(userInput == 'c'){
            previousTime = currentTime;
            currentTime = millis();
            
            data = analogRead(analogPin);   
            Serial.print(data);
            Serial.print('-');
            Serial.print(currentTime-previousTime);
            Serial.println("ms"); 
            
      } // if user input 'c'
   } // Serial.available
} // Void Loop



