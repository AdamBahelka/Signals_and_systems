// Signals and Systems: Homework 1 
// Exercise 7: Multipath fading
// Ditu Alexandru (s4004027)
// Bahelka Adam (s4887832)

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define PI 3.14159265358979323846

const double speed_of_light=3e8; // speed of light
const double frequency=150e6; // frequency

// Phase difference calculation, using the formula
double calculatePhaseDiff(double directDist, double reflectedDist) {
    double phaseDiff=2*PI*frequency*(reflectedDist-directDist)/speed_of_light;
    return phaseDiff;
}

int main() {
    int dr, dt, x;
    scanf("%d %d %d", &dr, &dt, &x); // getting the input
    // The direct path is just a straight line
    double directDist=x;
    // Calculate the reflected path distance using the Pythagorean theorem
    double reflectedDist=sqrt(pow(dr-x, 2)+pow(dt, 2))+sqrt(pow(dr, 2)+pow(dt, 2));
    // Call that function to do the phase difference calculation
    double phaseDiff=calculatePhaseDiff(directDist, reflectedDist);
    // Calculate the amplitude
    double receivedSignalAmplitude=fabs(2*cos(phaseDiff/2));
    // Output
    printf("%.2f\n", receivedSignalAmplitude);
}
