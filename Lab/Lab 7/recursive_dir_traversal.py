import os
import sys


def find_files(path):
    filecounter = pythonfilecounter = 0

    if os.path.isfile(path)== True:
        filecounter += 1
        if path.endswith('.py') == True:
            pythonfilecounter += 1
    else:
        files = os.listdir(path)
        for file in files:
            add = os.path.join(path,file)
            return add
    return filecounter, pythonfilecounter


def main():
    filecounter, pythonfilecounter = find_files(sys.argv[1])
    print("The total number of file: ", str(filecounter), "The total number of python file: ", str(pythonfilecounter))

main()