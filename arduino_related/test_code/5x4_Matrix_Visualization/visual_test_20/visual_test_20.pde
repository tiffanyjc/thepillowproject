/*
 Reads 20 analog inputs and visualizes them by drawing a 5x4 grid,
 using grayscale shading of each square to represent sensor value.
 */

import processing.serial.*;

Serial myPort;  // The serial port
int maxNumberOfSensors = 20;     
float[] sensorValue = new float[maxNumberOfSensors];  // global variable for storing mapped sensor values
float[] previousValue = new float[maxNumberOfSensors];  // array of previous values
int rectSize = 200;

int row = 4;
int col = 5;
int margin = 100;

void setup () { 
  size(1200, 1000);  // set up the window to whatever size you want
  //println(Serial.list());  // List all the available serial ports
  String portName = Serial.list()[0];
  myPort = new Serial(this, portName, 9600);
  myPort.clear();
  myPort.bufferUntil('\n');  // don't generate a serialEvent() until you get a newline (\n) byte
  background(255);    // set inital background
  smooth();  // turn on antialiasing
  rectMode(CORNER);
}


void draw () {
  
  //first row:
  for (int i = 0; i < col; i++ ) {
    fill(sensorValue[i]);
    rect(width - margin - rectSize * (i+1), margin + rectSize * 3, rectSize, rectSize);
  } 
  
  //second row:
  for (int j = 5; j < (col + 5); j++ ) {
    fill(sensorValue[j]);
    rect(width - margin - rectSize * (j-4), margin + rectSize * 2, rectSize, rectSize);
  }
  
  //third row:
  for (int k = 10; k < (col + 10); k++) {
    fill(sensorValue[k]);
    rect(width - margin - rectSize * (k-9),  margin + rectSize * 1, rectSize, rectSize);
  }  
  
  //fourth row:
   for (int l = 15; l < (col + 15); l++) {
    fill(sensorValue[l]);
    rect(width - margin - rectSize * (l-14),  margin + rectSize * 0, rectSize, rectSize);
  } 
  
  
  //fill(sensorValue[0]);
  //rect(width/5-rectSize, height/4-rectSize, rectSize,rectSize);  //top left
  
  //fill(sensorValue[1]);
  //rect(width/5, height/4-rectSize, rectSize,rectSize);  //top right
  
  //fill(sensorValue[2]);
  //rect(width/5-rectSize, height/4, rectSize,rectSize);  //bottom left
  
 //fill(sensorValue[3]);
  //rect(width/5, height/4, rectSize,rectSize);  //bottom right 
}


void serialEvent (Serial myPort) {
  String inString = myPort.readStringUntil('\n');  // get the ASCII string
  println(inString);

  if (inString != null) {  // if it's not empty
    inString = trim(inString);  // trim off any whitespace
    int incomingValues[] = int(split(inString, ","));  // convert to an array of ints

    //println("string length" + incomingValues.length);
    
    if (incomingValues.length <= maxNumberOfSensors && incomingValues.length > 0) {
      for (int i = 0; i < incomingValues.length; i++) {
        // map the incoming values (0 to  1023) to an appropriate gray-scale range (0-255):
        sensorValue[i] = map(incomingValues[i], 0, 10, 255, 0);  
       // println(i + "value: " + sensorValue[i]);
      }
    }
  }
}
