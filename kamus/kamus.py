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
        if len(term) > 1:
            return "kamus/" + self.__path + "/" + self.__lang + "/" + term[0] + "/" + term[0:2] + ".txt"
        else:
            return "kamus/" + self.__path + "/" + self.__lang + "/" + term[0] + "/" + term + ".txt"

    def __has_file(self, file_name):
        return os.path.isfile(file_name)

    def __load_kamus_file(self, term):
        fullpath = self.__get_file_name(term)
        if self.__has_file(fullpath):
            with open(fullpath) as cf:
                my_kamus = {
                    row['term']: {'tag': row['tag']}
                    for row in csv.DictReader(cf, skipinitialspace=True, delimiter=',')
                }
                if len(term) > 1:
                    self.__kamus[term[0]][term[0:2]] = my_kamus
                else:
                    self.__kamus[term[0]][term] = my_kamus

        else:
            if len(term) > 1:
                self.__kamus[term[0]][term[0:2]] = {}
            else:
                self.__kamus[term[0]][term] = {}


    def __save_kamus_file(self, file_name):
        with open(file_name, mode='w') as cf:
            fields = ['term','tag']
            writer = csv.DictWriter(cf, delimiter=',', fieldnames=fields)
            writer.writeheader()
            for abjad in self.__kamus.values():
                for grup in abjad.values():
                    for k,v in grup.items():
                        writer.writerow({'term':k,'tag':v.get('tag')})

    def __save_kamus_dir(self, dir):
        for ka,abjad in self.__kamus.items():
            for kg,grup in abjad.items():
                dirs = dir + os.altsep + ka
                if not os.path.exists(dirs):
                    os.makedirs(dirs)

                file_name = dirs + os.altsep + kg + os.extsep + "txt"

                with open(file_name, mode='w') as cf:
                    fields = ['term', 'tag']
                    writer = csv.DictWriter(cf, delimiter=',', fieldnames=fields)
                    writer.writeheader()

                    for k, v in grup.items():
                        writer.writerow({'term': k, 'tag': v.get('tag')})




    def save_kamus(self, file_name):
        self.__save_kamus_file(file_name)
        print "=Kamus disimpan di " + file_name

    def save_kamus_dir(self, dir):
        self.__save_kamus_dir(dir)
        print "Kamus disimpan di " + dir


    def load_kamus(self, term):
        term = str.lower(term)
        if not self.has_kamus_loaded(term):
            self.__load_kamus_file(term)

    def update_kamus(self, new_tuple):
        if len(new_tuple) != 2:
            return False

        term = str.lower(new_tuple[0].encode('utf-8'))
        tag = str.upper(new_tuple[1].encode('utf-8'))

        if self.has_non_alpha(term):
            return False

        if term[0] not in self.__kamus:
            self.__kamus[term[0]] = {}

        if term[0:2] not in self.__kamus[term[0]]:
            self.__kamus[term[0]][term[0:2]] = {}

        if len(term) > 1:
            if term in self.__kamus[term[0]][term[0:2]]:
                self.__kamus[term[0]][term[0:2]][term]['tag'] = tag
            else:
                self.__kamus[term[0]][term[0:2]][term] = {'tag':tag}
        else:
            if term in self.__kamus[term[0]][term[0]]:
                self.__kamus[term[0]][term[0]][term]['tag'] = tag
            else:
                self.__kamus[term[0]][term[0]][term] = {'tag':tag}

    def has_kamus_loaded(self, term):
        term = str.lower(term)
        if term[0] not in self.__kamus:
            self.__kamus[term[0]] = {}

        return term[0:2] in self.__kamus[term[0]]

    def has_non_alpha(self, term):
        term = str.lower(term)
        return not re.match(r"^[A-Za-z]+[\w]+", term)

    def get_class(self):
        return self.__class__.__name__

    def get_tag(self, term):
        term = str.lower(term)
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