import numpy as np

def is_fir_filter(x, y):
    # Length of input and output
    len_x, len_y = len(x), len(y)

    # The length of the impulse response
    len_h = len_y - len_x + 1

    # Check if the system can be an FIR filter
    if len_h <= 0:
        return False, None

    # Construct the matrix for the linear system
    A = np.zeros((len_y, len_h))
    for i in range(len_h):
        A[i:len_x+i, i] = x

    # Solve the linear system
    try:
        h = np.linalg.lstsq(A, y, rcond=None)[0]
        return True, h
    except np.linalg.LinAlgError:
        return False, None

def main():
    # Example input
    x = [1, -1]
    y = [4, -2, 2, -2, -2]

    is_fir, h = is_fir_filter(x, y)

    if is_fir:
        print(f"{len(h)}: {h.tolist()}")
    else:
        print("NO FIR")

main()
