import cmath

def calculate_impulse_response(angles):

    M = len(angles)
    
    impulse_response = [0] * (M + 1)
    
    impulse_response[0] = 1
    
    for angle in angles:
        root = cmath.exp(complex(0, angle))
        
        for i in range(M, 0, -1):
            impulse_response[i] -= impulse_response[i-1] * root
    
    impulse_response = [round(x.real, 2) for x in impulse_response]
    
    return impulse_response

def read_signal():
    input_line = input().strip()
    return input_line

def printSignal(length, signal):
    print(f"{length}: {signal}")

def main(): 
    useless = read_signal()
    angles = list(map(float, read_signal().split()))

    impulse_response = calculate_impulse_response(angles)

    printSignal(len(impulse_response), impulse_response)

if __name__ == "__main__":
    main()