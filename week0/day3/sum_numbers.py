import sys


def main():
    sum = 0
    filename = sys.argv[1]
    file = open(filename, "r")
    numbers = file.read().split(" ")
    for step in range(0, len(numbers)):
        sum += int(numbers[step])
    print(sum)

if __name__ == '__main__':
    main()