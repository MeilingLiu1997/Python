import re
import os
import sys
from os import listdir
from os.path import isfile, join


def main():
    mypath = sys.argv[1]
    dictionary = {}
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for i in onlyfiles:
        if i.endswith('.txt'):
            file = os.path.join(mypath,i)
            txtfile = open(file, "r", encoding="ISO-8859-1")
            line = txtfile.readline()
            while line:
                values = re.findall(r"[\w']+", line)
                line = txtfile.readline()
                for word in values:
                    if word not in dictionary:
                        dictionary[word] = 1
                    else:
                        dictionary[word] += 1
            txtfile.close()
    print(dictionary)
    html_file = open('word-frequency.html', 'w')
    html_file.write('<!DOCTYPE html> <html> <head> <strong>Words count chart</strong> </head> '
                    '<body><table border="1px"><tr><th>Words</th><th>Counts</th></tr>')

    for word in dictionary:
        if dictionary[word] >= 50:
            html_file.write('<td>' + str(word) + '</td>' + '\n')
            html_file.write('<td>' + str(dictionary[word]) + '</td>' + '\n')
            html_file.write('<tr>'+'</tr>')
    html_file.close()

main()