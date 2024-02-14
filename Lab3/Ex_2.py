import math

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return "{:.2f}+j{:.2f}".format(self.real, self.imag) if self.imag >= 0 else "{:.2f}-j{:.2f}".format(self.real, -self.imag)


def create_vandermonde_matrix(N):
    # w = e^(-j2π/N)
    w = Complex(math.cos(-2 * math.pi / N), math.sin(-2 * math.pi / N))
    W = []
    for i in range(N):
        row = []
        for j in range(N):
            # w^(i*j)
            w_ij = pow(w, i * j)
            row.append(w_ij)
        W.append(row)
    return W


def pow(base, exponent):
    result = Complex(1, 0)  # Start with the complex number 1 + 0j
    for _ in range(exponent):
        result = result * base
    return result


def discrete_fourier_transform(x, N):
    W = create_vandermonde_matrix(N)
    X = []
    for i in range(N):
        sum = Complex(0, 0)
        for j in range(N):
            sum = sum + (W[i][j] * Complex(x[j], 0))
        X.append(sum)
    return X


def read_signal():
    input_line = input().strip()
    length = int(input_line.split(':')[0])
    signal = list(map(int, input_line.split(':')[1].strip()[1:-1].split(',')))
    return signal, length


def print_signal(signal):
    for s in signal:
        print(str(s), end=", ")


def main():
    signal, length = read_signal()
    X = discrete_fourier_transform(signal, length)
    print_signal( [str(x) for x in X])


if __name__ == "__main__":
    main()
