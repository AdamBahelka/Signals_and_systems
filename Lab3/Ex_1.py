import math

def pearson_correlation(x, h):
    x_mean = sum(x) / len(x)
    h_mean = sum(h) / len(h)
    numerator = sum((x_i - x_mean) * (h_i - h_mean) for x_i, h_i in zip(x, h))
    denominator = math.sqrt(sum((x_i - x_mean) ** 2 for x_i in x) * sum((h_i - h_mean) ** 2 for h_i in h))
    
    return 0 if denominator == 0 else numerator / denominator

def calculate_sequence(signal, template):
    L = len(template)
    correlations = []
    
    for n in range(len(signal) - L + 1):
        x = signal[n:n + L]
        correlation = pearson_correlation(x, template)
        correlations.append(round(correlation, 5))
    
    return correlations

def read_signal():
    input_line = input().strip()
    length = int(input_line.split(':')[0])
    signal = list(map(int, input_line.split(':')[1].strip()[1:-1].split(',')))
    return signal, length

def printSignal(length, signal):
    print(f"{length}: {signal}")

def main():
    h, length_h = read_signal()
    x, length_x = read_signal()
    correlations = calculate_sequence(x, h)
    printSignal(len(correlations), correlations)

if __name__ == "__main__":
    main()