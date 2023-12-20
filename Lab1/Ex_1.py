#  Signals and Systems: Homework 1 
#  Exercise 7: Multipath fading
#  Ditu Alexandru (s4004027)
#  Bahelka Adam (s4887832)
import math

def get_input_data():
    x, y = map(int, input().split())
    return x, y

def convert_to_polar(x, y):
    # Calculate r
    r = math.sqrt(x**2 + y**2)
    # Calculate θ in radians
    theta = math.atan2(y, x)
    return (r, theta)

def print_output_data(output_data):
    # Print each value in the output_data tuple with two decimal places
    print("{:.2f} {:.2f}".format(output_data[0], output_data[1]))


def main():
    x, y = get_input_data()
    polar_coordinates = convert_to_polar(x, y)
    print_output_data(polar_coordinates)

if __name__ == "__main__":
    main()




