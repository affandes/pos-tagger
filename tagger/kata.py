# Class kata

class Kata():

    __teks = ''
    __tag = ''

    def __init__(self, teks, tag = ''):
        self.__teks = teks
        self.__tag = tag

    def __str__(self):
        return '{}/{}'.format(self.__teks, self.__tag)

    def set_tag(self, tag = ''):
        self.__tag = tag