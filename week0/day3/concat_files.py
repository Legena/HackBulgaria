import sys


def main():
    file = open("MEGATRON", "a")
    for file_num in range(1, len(sys.argv)):
        opened_file = open(sys.argv[file_num], "r")
        file.write(opened_file.read() + '\n')
    file.write('\n')

if __name__ == '__main__':
    main()