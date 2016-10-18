import re


class FileProcessor:
    def __init__(self, content):
        self.content = content
        self.author = None
        self.section = None
        self.keywords = None
        self.sentences = None
        self.shortcuts = None
        self.integers = None
        self.floats = None
        self.dates = None
        self.emails = None

    def process(self):
        self.__match_author()
        self.__match_section()
        self.__match_keywords()
        self.__match_sentences()
        self.__match_shortcuts()
        self.__match_integers()
        self.__match_floats()
        self.__match_dates()
        self.__match_emails()

    def __match_author(self):
        m = re.search('<META NAME="AUTOR" CONTENT="(.*)">', self.content)

        self.author = m.group(1)

    def __match_section(self):
        m = re.search('<META NAME="DZIAL" CONTENT="(.*)">', self.content)

        self.section = m.group(1)

    def __match_keywords(self):
        self.keywords = []

    def __match_sentences(self):
        self.sentences = []

    def __match_shortcuts(self):
        self.shortcuts = []

    def __match_integers(self):
        pattern = r'(-[1-3][0-2][0-7][0-6][0-8]|[1-3][0-2][0-7][0-6][0-7]|-?[1-9][0-9]{,3})'
        regex = re.compile(pattern)
        self.integers = regex.findall(self.content)

    def __match_floats(self):
        self.floats = []

    def __match_dates(self):
        self.dates = []

    def __match_emails(self):
        self.emails = []
