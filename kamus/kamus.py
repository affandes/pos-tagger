# Fungsi untuk kamus

import csv
import re
import os


class Kamus():

    __kamus = {}
    __path = ''
    __lang = ''
    __notag = 'x'

    def __init__(self, lang='id', path='default'):
        self.__path = path
        self.__lang = lang

    def __get_file_name(self, term):
        return "kamus/" + self.__path + "/" + self.__lang + "/" + term[0] + "/" + term + ".txt"

    def __has_file(self, file_name):
        return os.path.isfile(file_name)

    def __load_kamus_file(self, file_name):
        if self.__has_file(file_name):
            with open(file_name) as cf:
                my_kamus = {
                    row['term']: {'tag': row['tag']}
                    for row in csv.DictReader(cf, skipinitialspace=True, delimiter=',')
                }
                self.__kamus[file_name[0]][file_name] = my_kamus

        else:
            self.__kamus[file_name[0]][file_name] = {}


    def load_kamus(self, term):
        if not self.has_kamus_loaded(term):
            if len(term) > 1:
                self.__load_kamus_file(term[0:2])
            else:
                self.__load_kamus_file(term[0])

    def has_kamus_loaded(self, term):
        if term[0] not in self.__kamus:
            self.__kamus[term[0]] = {}

        return term[0:2] in self.__kamus[term[0]]

    def has_non_alpha(self, term):
        return not re.match(r"^[A-Za-z]+[\w]+", term)

    def get_class(self):
        return self.__class__.__name__

    def get_tag(self, term):
        if self.has_non_alpha(term):
            return self.__notag

        if not self.has_kamus_loaded(term):
            self.load_kamus(term)

        if len(term) > 1:
            if term in self.__kamus[term[0]][term[0:2]]:
                return self.__kamus[term[0]][term[0:2]][term]['tag']
            else:
                return self.__notag
        else:
            if term in self.__kamus[term[0]][term[0]]:
                return self.__kamus[term[0]][term[0]][term]['tag']
            else:
                return self.__notag