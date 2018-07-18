/*
5x4 presure sensor matrix code, 
 where each row/column is connected to an individual analog pin

 */

 #include <MuxShield.h>

//Initialize the Mux Shield
MuxShield muxShield;

int sensorValues[] = {0,0,0,0};

int numPin1 = 16;
int numPin2 = 4;

void setup() {
  
  //Set I/O 1, I/O 2, and I/O 3 as analog inputs
  muxShield.setMode(1,ANALOG_IN);
  muxShield.setMode(2,ANALOG_IN);
  //muxShield.setMode(3,ANALOG_IN);

  Serial.begin(9600);
}

//Arrays to store analog values after recieving them
int IO1AnalogVals[4];
int IO2AnalogVals[16];
//int IO3AnalogVals[];

void loop() {

  for (int i = 0; i < numPin1; i ++) {
    IO2AnalogVals[i] = muxShield.analogReadMS(2,i);
  }

  for (int j = 0; j < numPin2; j ++) {
    IO1AnalogVals[j] = muxShield.analogReadMS(1,j);
  }

//  Serial.println("IO2&3");
  
  for (int k = 0; k < numPin1; k ++) {
    Serial.print(IO2AnalogVals[k]);
    Serial.print(','); 
  }

  for (int l = 0; l < numPin2; l ++) {
    if (l <= numPin2 - 2) {
      Serial.print(IO1AnalogVals[l]);
      Serial.print(','); 
    } else {
      Serial.print(IO1AnalogVals[l]);
    }
  }

  Serial.println();
}





