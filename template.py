from __future__ import print_function
import os
import sys
import codecs

from FileProcessor import FileProcessor


def process_file(filepath):
    fp = codecs.open(filepath, 'rU', 'iso-8859-2')

    content = fp.read()

    file_processor = FileProcessor(content)
    file_processor.process()

    fp.close()
    print("nazwa pliku:", filepath)
    print("autor:", file_processor.author)
    print("dzial:", file_processor.section)
    print("slowa kluczowe:", ", ".join(file_processor.keywords))
    print("liczba zdan:", len(file_processor.sentences))
    print("liczba skrotow:", len(file_processor.shortcuts))
    print("liczba liczb calkowitych z zakresu int:", len(file_processor.integers))
    print("liczba liczb zmiennoprzecinkowych:", len(file_processor.floats))
    print("liczba dat:", len(file_processor.dates))
    print("liczba adresow email:", len(file_processor.emails))
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
