import math

def get_input_data():
    # Reading two floating point numbers from input
    r, theta = map(float, input().split())
    return r, theta

def convert_to_cartesian(r, theta):
    # Calculate x and y
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

def print_output_data(output_data):
    # Print each value in the output_data tuple with two decimal places
    print("{:.2f} {:.2f}".format(output_data[0], output_data[1]))

def main():
    r, theta = get_input_data()
    cartesian_coordinates = convert_to_cartesian(r, theta)
    print_output_data(cartesian_coordinates)

if __name__ == "__main__":
    main()
