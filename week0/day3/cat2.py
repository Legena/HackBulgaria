# cat2.py
import sys


def main():
    for input_file in range(1, len(sys.argv)):
        file = open(sys.argv[input_file], "r")
        print(file.read())

if __name__ == '__main__':
    main()