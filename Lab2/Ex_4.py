import math

def readSignal():
    input_line = input().strip()
    length = int(input_line.split(':')[0])
    signal = list(map(int, input_line.split(':')[1].strip()[1:-1].split(',')))
    return signal, length

def calculate_frequency_response(h, Ax, omega, phi_x):
    # Calculate the frequency response of the FIR filter
    real_part = 0
    imag_part = 0
    for n, hn in enumerate(h):
        real_part += hn * math.cos(-omega * n)
        imag_part += hn * math.sin(-omega * n)

    # Magnitude and phase of the frequency response
    magnitude = math.sqrt(real_part**2 + imag_part**2)
    phase = math.atan2(imag_part, real_part)

    # Calculate Ay and φy
    Ay = Ax * magnitude
    phi_y = phi_x + phase

    # Normalize φy to be within -π to π
    while phi_y > math.pi:
        phi_y -= 2 * math.pi
    while phi_y <= -math.pi:
        phi_y += 2 * math.pi

    return Ay, omega, phi_y

def main():
    # Read the impulse response h[n]
    h, _ = readSignal()

    # Read Ax, ω̂, and φx
    Ax, omega, phi_x = map(float, input().split())

    # Calculate the output signal parameters
    Ay, omega, phi_y = calculate_frequency_response(h, Ax, omega, phi_x)

    # Print the output signal
    if Ay == 0:
        print("y[n]=0.00")
    else:
        print(f"y[n]={Ay:.2f}cos({omega:.2f}*n+{phi_y:.2f})")

if __name__ == "__main__":
    main()
