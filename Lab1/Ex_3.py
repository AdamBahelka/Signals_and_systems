import math

def get_input_data():
    # Reading frequency and number of sinusoids
    f, n = map(int, input().split())
    sinusoids = []
    for _ in range(n):
        amplitude, phase = map(float, input().split())
        sinusoids.append((amplitude, phase))
    return f, sinusoids

def sum_sinusoids(f, sinusoids):
    # Summing the sinusoids manually
    sum_real = 0
    sum_imag = 0
    for amplitude, phase in sinusoids:
        sum_real += amplitude * math.cos(phase)
        sum_imag += amplitude * math.sin(phase)

    # Calculating amplitude and phase of the resulting sinusoid
    A = math.sqrt(sum_real**2 + sum_imag**2)
    phi = math.atan2(sum_imag, sum_real)
    return A, phi

def print_output_data(f, A, phi):
    if A == 0:
        print("x(t)=0.00")
    else:
        # Adjusting phase to match the formula
        phi_adjusted = phi % (2 * math.pi)
        print("x(t)={:.2f}cos(2*pi*{}*t+{:.2f})".format(A, f, phi_adjusted))

def main():
    f, sinusoids = get_input_data()
    A, phi = sum_sinusoids(f, sinusoids)
    print_output_data(f, A, phi)

if __name__ == "__main__":
    main()
