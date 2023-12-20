def custom_convolution(h, x):
    # Lengths of the input signal and the filter
    len_x = len(x)
    len_h = len(h)

    # Initialize the output signal with zeros
    y = [0] * (len_x + len_h - 1)

    # Perform the convolution operation
    for i in range(len_x):
        for j in range(len_h):
            y[i + j] += x[i] * h[j]

    return y

def readSignal():
    input_line = input().strip()
    length = int(input_line.split(':')[0])
    signal = list(map(int, input_line.split(':')[1].strip()[1:-1].split(',')))
    return signal, length

def printSignal(length, signal):
    print(f"{length}: {signal}")

def main():
    # Read the number of FIR filters
    k = int(input())

    # Read the FIR filter kernels
    filters = [readSignal()[0] for _ in range(k)]

    # Read the input signal
    x, _ = readSignal()

    # Apply each filter in the cascade
    for h in filters:
        x = custom_convolution(h, x)

    # Print the final output signal
    printSignal(len(x), x)

if __name__ == "__main__":
    main()