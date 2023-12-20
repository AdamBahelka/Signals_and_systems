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
    # Read the first signal (kernel)
    h, _ = readSignal()
    # Read the second signal (input)
    x, _ = readSignal()

    # Apply FIR filter
    y = custom_convolution(h, x)

    # Print the output signal
    printSignal(len(y), y)

if __name__ == "__main__":
    main()
