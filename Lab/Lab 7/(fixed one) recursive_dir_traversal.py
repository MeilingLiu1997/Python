import os
import sys


def find_files(path):
    filecounter = pythonfilecounter = 0
    if os.path.isfile(path):
        basename = os.path.basename(path)
        filecounter += 1
        if basename.endswith('.py'):
            pythonfilecounter += 1
        elif basename == '.DS_Store':
            return 0, 0
    else:
        files = os.listdir(path)
        for file in files:
            result = find_files(os.path.join(path,file))
            filecounter += result[0]
            pythonfilecounter += result[1]

    return filecounter, pythonfilecounter


def main():
    filecounter, pythonfilecounter = find_files(sys.argv[1])

    print("The total number of file: ", str(filecounter), "The total number of python file: ", str(pythonfilecounter))

main()