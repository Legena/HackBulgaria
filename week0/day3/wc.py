import sys


def main():
    filename = sys.argv[2]
    file = open(filename, "r")
    file_content = file.read()
    if (sys.argv[1] == "chars"):
        print(len(file_content))
    elif (sys.argv[1] == "words"):
        print(file_content.count(" ") + file_content.count("\n")
        - file_content.count("\n\n"))
    elif (sys.argv[1] == "lines"):
        print(file_content.count("\n") + 1)

if __name__ == '__main__':
    main()