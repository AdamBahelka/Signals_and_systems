def find_impulse_response(x, y):
    len_x = len(x)
    len_y = len(y)
    len_h = len_y - len_x + 1

    if len_h <= 0 or x[0] == 0:
        return "NO FIR"

    # Initialize h with zeros
    h = [0] * len_h

    # Basic deconvolution to estimate h
    for i in range(len_h):
        h[i] = round(y[i] / x[0])
        for j in range(1, len_x):
            if i - j >= 0:
                y[i] -= h[i - j] * x[j]

    return h

def readSignal():
    input_line = input().strip()
    length = int(input_line.split(':')[0])
    signal = list(map(int, input_line.split(':')[1].strip()[1:-1].split(',')))
    return signal, length

def printSignal(length, signal):
    print(f"{length}: {signal}")

def main():
    # Read the input signal x[n]
    x, _ = readSignal()
    # Read the output signal y[n]
    y, _ = readSignal()

    # Find the impulse response h[n]
    h = find_impulse_response(x, y)

    # Print the impulse response or "NO FIR"
    if isinstance(h, str):
        print(h)
    else:
        printSignal(len(h), h)

if __name__ == "__main__":
    main()
