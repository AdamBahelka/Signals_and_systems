import cmath

def calculate_impulse_response(angles):
    """
    Calculate the impulse response from the given angles of the roots in the z-domain.
    The roots are given in radians and are assumed to be on the unit circle.
    """
    # Number of roots
    M = len(angles)
    
    # Initialize the impulse response array with zeros
    impulse_response = [0] * (M + 1)
    
    # The impulse response of a FIR filter is the inverse Z-transform of the transfer function.
    # For a system function defined by its roots, the transfer function is the product of (1 - root * z^-1)
    # We start with an impulse response that would correspond to a system function with no roots (a single 1).
    impulse_response[0] = 1
    
    # Calculate the impulse response by iteratively multiplying the current impulse response by (1 - root * z^-1)
    # for each root. This is done by convolution in the time domain.
    for angle in angles:
        # Calculate the root in the z-domain
        root = cmath.exp(complex(0, angle))
        
        # For each root, update the impulse response
        for i in range(M, 0, -1):
            impulse_response[i] -= impulse_response[i-1] * root
    
    # Since the impulse response is real, we take the real part and round to 2 decimal places
    impulse_response = [round(x.real, 2) for x in impulse_response]
    
    # Remove the 0th element as it corresponds to the direct path and is always 1 due to the filter being causal
    return impulse_response

def read_signal():
    input_line = input().strip()
    return input_line

def printSignal(length, signal):
    print(f"{length}: {signal}")

def main(): 
    useless = read_signal()
    angles = list(map(float, read_signal().split(',')))

    # Compute the impulse response
    impulse_response = calculate_impulse_response(angles)

    # Print the impulse response
    printSignal(len(impulse_response), impulse_response)

if __name__ == "__main__":
    main()