import math

def get_input_data():
    # Reading two integers from input
    f0, fs = map(int, input().split())
    return f0, fs

def calculate_alias_frequency(f0, fs):
    # Calculate the aliased frequency
    k = math.floor(f0 / fs)
    f_alias = abs(f0 - k * fs)
    return f_alias

def print_output_data(output_data):
    # Print the output data as an integer
    print("{}".format(output_data))

def main():
    f0, fs = get_input_data()
    alias_frequency = calculate_alias_frequency(f0, fs)
    print_output_data(alias_frequency)

if __name__ == "__main__":
    main()