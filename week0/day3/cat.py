# cat.py
import sys


def main():
    filename = sys.argv[1]
    file = open(filename, "r")
    print(file.read())

if __name__ == '__main__':
    main()
