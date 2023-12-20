import numpy as np
from PIL import Image
import sys

class GrayImage:
    '''
    Class to store gray-scale images
    '''
    def __init__(self, width, height, data):
        self.width = width
        self.height = height
        self.data = data

def readPGM(filename):
    '''
    Function to read PGM images
    '''
    image = Image.open(filename)
    image = image.convert('L')
    width, height = image.size
    img = GrayImage(width, height)
    img.data = np.array(image)
    return img

def writePGM(filename, image):
    '''
    Function to write PGM images'''
    im = Image.fromarray(image.data)
    im.save(filename)

def convolveImage(operandOne, operandTwo):
    # Implement this functionality
    return output

def performSobelEdgeDetection(image):
    # Implement this functionality
    # Hint: use convolveImage() function
    return output

def main():
    filename = input().strip()

    # read input image
    image = readPGM(filename)

    # process image
    output = performSobelEdgeDetection(image)

    # generate output
    total = np.sum(output.data)
    print(total)
    writePGM("output.pgm", output)

if __name__ == "__main__":
    main()