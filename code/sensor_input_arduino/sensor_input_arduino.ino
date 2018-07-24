#include <SD.h>
 #include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <MuxShield.h>

  
Adafruit_BNO055 bno = Adafruit_BNO055(55);
 const int sampleWindow = 50; // Sample window width in mS (50 mS = 20Hz)
unsigned int sample;
int l = 0; 
unsigned long time; 

//Initialize the Mux Shield
MuxShield muxShield;

int numPin1 = 16;
int numPin2 = 4;

int noiseFilter = 10;

void setup(void) 
{
  //Set I/O 1, I/O 2, and I/O 3 as analog inputs
  muxShield.setMode(1,ANALOG_IN);
  muxShield.setMode(2,ANALOG_IN);
  //muxShield.setMode(3,ANALOG_IN);
  
//  Serial.println("Orientation Sensor Test"); Serial.println("");
  Serial.begin(9600);
  
  /* Initialise the sensor */
  if(!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
    
  bno.setExtCrystalUse(true);
}

//Arrays to store analog values after recieving them
int IO1AnalogVals[4];
int IO2AnalogVals[16];
//int IO3AnalogVals[];

 
void loop(void) 
{
//  /* Get a new sensor event */ 
  sensors_event_t event; 
  bno.getEvent(&event);
  imu::Vector<3> accel = bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  imu::Vector<3> gyro = bno.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE);
  imu::Vector<3> euler = bno.getVector(Adafruit_BNO055::VECTOR_EULER);

// keep all the spaces to separate data! python will read this as a very long string 
// get time 
time = millis(); 
Serial.print((float) time / 1000); 
Serial.print(" "); 

//   printing accel data
  Serial.print(accel.x(), 4); 
  Serial.print(" "); 
  Serial.print(accel.y(), 4); 
  Serial.print(" "); 
  Serial.print(accel.z(), 4); 
  Serial.print(" "); 

  //   printing gyroscope data
  Serial.print(gyro.x(), 4); 
  Serial.print(" "); 
  Serial.print(gyro.y(), 4); 
  Serial.print(" "); 
  Serial.print(gyro.z(), 4); 
Serial.print(" "); 

    //   printing orientation data
  Serial.print(euler.x(), 4); 
  Serial.print(" "); 
  Serial.print(euler.y(), 4); 
  Serial.print(" "); 
  Serial.print(euler.z(), 4); 
  Serial.print(" "); 


  // this is the same thing as printing orientation 
////  /* Display the floating point data */
//  Serial.print(event.orientation.x, 4);
//  Serial.print(" "); 
//  Serial.print(event.orientation.y, 4);
//  Serial.print(" "); 
//  Serial.print(event.orientation.z, 4);
//  Serial.print(" "); 


// microphone stuff 

   unsigned long startMillis= millis();  // Start of sample window
   unsigned int peakToPeak = 0;   // peak-to-peak level

   unsigned int signalMax = 0;
   unsigned int signalMin = 1024;

   // collect data for 50 mS
   while (millis() - startMillis < sampleWindow)
   {
      sample = analogRead(0);
      if (sample < 1024)  // toss out spurious readings
      {
         if (sample > signalMax)
         {
            signalMax = sample;  // save just the max levels
         }
         else if (sample < signalMin)
         {
            signalMin = sample;  // save just the min levels
         }
      }
   }
   peakToPeak = signalMax - signalMin;  // max - min = peak-peak amplitude
   double volts = (peakToPeak * 5.0) / 1024;  // convert to volts

   Serial.print(volts);
   Serial.print(" "); 

   // end microphone stuff
   
   //FSR Pressure Grid
   
    for (int i = 0; i < numPin1; i ++) {
      if (muxShield.analogReadMS(2,i) > noiseFilter) {
        IO2AnalogVals[i] = muxShield.analogReadMS(2,i);
      } else {
        IO2AnalogVals[i] = 0;
      }
    }

    for (int j = 0; j < numPin2; j ++) {
       if (muxShield.analogReadMS(1,j) > noiseFilter) {
         IO1AnalogVals[j] = muxShield.analogReadMS(1,j);
      } else {
         IO1AnalogVals[j] = 0;
      }
    }
      
    for (int k = 0; k < numPin1; k ++) {
      Serial.print(IO2AnalogVals[k]);
      Serial.print(' '); 
    }

    for (int l = 0; l < numPin2; l ++) {
      if (l <= numPin2 -2) {
        Serial.print(IO1AnalogVals[l]);
        Serial.print(' '); 
      } else {
        Serial.print(IO1AnalogVals[l]);
      }
    }
    
    Serial.println();
   
    delay(250); 
}


