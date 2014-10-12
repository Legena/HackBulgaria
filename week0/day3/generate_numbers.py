# generate_numbers.py
import sys
from random import randint


def main():
    filename = sys.argv[1]
    file = open(filename, "w")
    for count in range(0, int(sys.argv[2])):
        file.write(str(randint(1, 1000)) + " ")
    file.truncate(file.tell() - 1)

if __name__ == '__main__':
    main()
