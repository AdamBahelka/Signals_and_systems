def read_signal():
    input_line = input().strip()
    length = int(input_line.split(':')[0])
    signal = list(map(int, input_line.split(':')[1].strip()[1:-1].split(',')))
    return signal, length

def print_signal(length, signal):
    print(f"{length}: {signal}")

def solve_linear_system(matrix, output):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        # Find the max element in the current column
        max_el = abs(matrix[i][i])
        max_row = i
        for k in range(i+1, rows):
            if abs(matrix[k][i]) > max_el:
                max_el = abs(matrix[k][i])
                max_row = k

        # Swap the rows
        matrix[max_row], matrix[i] = matrix[i], matrix[max_row]
        output[max_row], output[i] = output[i], output[max_row]

        # Set to zero the lower elements in the column
        for k in range(i+1, rows):
            c = -matrix[k][i] / matrix[i][i]
            for j in range(i, cols):
                if i == j:
                    matrix[k][j] = 0
                else:
                    matrix[k][j] += c * matrix[i][j]
            output[k] += c * output[i]

    # Solve equation Ax=b for an upper triangular matrix A
    solution = [0 for _ in range(cols)]
    for i in range(rows-1, -1, -1):
        solution[i] = output[i] / matrix[i][i]
        for k in range(i-1, -1, -1):
            output[k] -= matrix[k][i] * solution[i]

    return solution


def main():
    x, len_x = read_signal()
    y, len_y = read_signal()

    # Check if the system can be a FIR system
    if len_y < len_x:
        print("NO FIR")
        return

    # Setup the system of linear equations
    matrix = [[0 for _ in range(len_y - len_x + 1)] for _ in range(len_y)]
    for i in range(len_y):
        for j in range(len_y - len_x + 1):
            if i - j >= 0 and i - j < len_x:
                matrix[i][j] = x[i - j]

    # Solve the system
    h = solve_linear_system(matrix, y)
    if h is None:
        print("NO FIR")
    else:
        print_signal(len_y - len_x + 1, h)

if __name__ == "__main__":
    main()
