from __future__ import print_function
import os
import sys
import re
import codecs


def process_file(filepath):
    fp = codecs.open(filepath, 'rU', 'iso-8859-2')

    content = fp.read()

    #
    #  INSERT YOUR CODE HERE
    #

    fp.close()
    print("nazwa pliku:", filepath)
    print("autor:")
    print("dzial:")
    print("slowa kluczowe:")
    print("liczba zdan:")
    print("liczba skrotow:")
    print("liczba liczb calkowitych z zakresu int:")
    print("liczba liczb zmiennoprzecinkowych:")
    print("liczba dat:")
    print("liczba adresow email:")
    print("\n")


try:
    path = sys.argv[1]
except IndexError:
    print("Brak podanej nazwy katalogu")
    sys.exit(0)

tree = os.walk(path)

for root, dirs, files in tree:
    for f in files:
        if f.endswith(".html"):
            filepath = os.path.join(root, f)
            process_file(filepath)
