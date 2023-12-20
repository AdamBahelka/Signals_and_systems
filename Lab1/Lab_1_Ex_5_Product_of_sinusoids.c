// Signals and Systems: Homework 1 
// Exercise 5: Products of sinusoids
// Ditu Alexandru (s4004027)
// Bahelka Adam (s4887832)

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_SIZE 100 // Max number of frequencies we can handle

// Function to compare two integers for qsort
int compareInts(const void *a, const void *b) {
    return (*(int *)a-*(int *)b);
}

// Add a new frequency to the list if it's not already there
void addUniqueFrequency(int newFreq, int *frequencies, int *totalFreqs) {
    for (int i=0; i<*totalFreqs; i++) {
        if (frequencies[i]==newFreq) {
            return; // Skip if we already have this frequency
        }
    }
    frequencies[(*totalFreqs)++]=newFreq; // Add new frequency
}

// Recursive function to generate the spectrum of frequencies
void buildSpectrum(int *inputFreqs, int n, int currentFreq, int *spectrum, int *spectrumSize, bool *isUsed) {
    if (n==0) {
        // Add the frequency if it's non-negative
        if (currentFreq>=0) {
            addUniqueFrequency(currentFreq, spectrum, spectrumSize);
        }
        return;
    }
    // Include the current frequency
    isUsed[n-1]=true; // Mark this frequency as used
    buildSpectrum(inputFreqs, n-1, currentFreq+inputFreqs[n-1], spectrum, spectrumSize, isUsed);
    // Exclude the current frequency
    buildSpectrum(inputFreqs, n-1, currentFreq-inputFreqs[n-1], spectrum, spectrumSize, isUsed);
    // Reset for next iteration
    isUsed[n-1]=false; // Reset
}

int main() {
    int inputFrequencies[MAX_SIZE];
    int spectrum[MAX_SIZE*MAX_SIZE]={0};
    bool usedFrequencies[MAX_SIZE]={false};
    int spectrumCount=0; 
    int freqCount=0;

    // Reading the input frequencies
    while (scanf("%d", &inputFrequencies[freqCount])&&inputFrequencies[freqCount]!=0) {
        freqCount++;
    }
    // Generating the spectrum
    buildSpectrum(inputFrequencies, freqCount, 0, spectrum, &spectrumCount, usedFrequencies);
    // Sorting the spectrum to get it in order
    qsort(spectrum, spectrumCount, sizeof(int), compareInts);
    // Outputting the sorted frequencies
    for (int i=0; i<spectrumCount; i++) {
        printf("%d\n", spectrum[i]);
    }
}

