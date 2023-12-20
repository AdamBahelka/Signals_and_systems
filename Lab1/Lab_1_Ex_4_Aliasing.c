// Signals and Systems: Homework 1 
// Exercise 4: Aliasing
// Ditu Alexandru (s4004027)
// Bahelka Adam (s4887832)

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// This function calculates the frequency after sampling, to check for aliasing.
float calculateFrequency(int signalFreq, int samplingFreq){
  int reconstructedFreq;
  
  // Check if sampling frequency is less than signal frequency
  if (samplingFreq<signalFreq) {
    float ratio, modifiedRatio;
    
    // We need to cast to float to get accurate division results
    ratio=(float)signalFreq/(float)samplingFreq;
    
    // The math here is to find the aliased frequency
    modifiedRatio=fmod(2*ratio,2.0);
    if (modifiedRatio>1) {
        modifiedRatio=2-modifiedRatio;
    }
    reconstructedFreq=(int)(modifiedRatio*samplingFreq/2);
  } else if (samplingFreq==signalFreq){ // If freqs are equal, no aliasing
    reconstructedFreq=0;
  } else if (samplingFreq>2*signalFreq) { // Nyquist Theorem stuff
    reconstructedFreq=signalFreq;
  } else { // Other cases: simple subtraction
    reconstructedFreq=samplingFreq-signalFreq;
  }
  
  return reconstructedFreq;
}

int main() {
  int signalFrequency, samplingFrequency, outputFrequency;

  // Get the input frequencies from the user
  scanf("%d %d", &signalFrequency, &samplingFrequency);
  
  // Calculate the frequency after sampling
  outputFrequency=calculateFrequency(signalFrequency, samplingFrequency);
  
  // Print the result
  printf("%d\n", outputFrequency);
}
