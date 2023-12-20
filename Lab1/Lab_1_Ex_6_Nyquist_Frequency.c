// Signals and Systems: Homework 1 
// Exercise 6: Nyquist frequency
// Ditu Alexandru (s4004027)
// Bahelka Adam (s4887832)

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void *safeMalloc(int sz) {
  void *p = calloc(sz, 1);
  if (p == NULL) {
    fprintf(stderr, "Fatal error: safeMalloc(%d) failed.\n", sz);
    exit(EXIT_FAILURE);
  }
  return p;
}

int *makeIntArray(int n) {
  return safeMalloc(n*sizeof(int));
}

// Function to read input frequencies
void readFrequencies(int **input, int *count, int *sum) {
    int capacity=5;
    *input=makeIntArray(capacity);
    *sum=0;
    *count=0;

    // Read frequencies from the keyboard
    while (scanf("%d", &(*input)[*count])==1) {
        // Stop if the input is 0
        if ((*input)[*count]==0) {
            break;
        }
        // Add the frequency to the sum
        *sum+=(*input)[*count];
        // Increment the count and reallocate if needed
        (*count)++;
        if (*count==capacity) {
            capacity+=5;
            *input=realloc(*input, capacity * sizeof(int));
        }
    }
}

// Function to calculate the Nyquist frequency
int calculateNyquistFrequency(int sum) {
    // Nyquist frequency is twice the sum of all frequencies
    return sum*2;
}

// Function to print the result
void printResult(int result) {
    printf("%d\n", result);
}

int main() {
    int *frequencies;
    int count;
    int sum;
    // Read frequencies from user input
    readFrequencies(&frequencies, &count, &sum);
    // Calculate the Nyquist frequency
    int nyquistFrequency=calculateNyquistFrequency(sum);
    // Output the Nyquist frequency
    printResult(nyquistFrequency);
    // Free the allocated memory
    free(frequencies);
}