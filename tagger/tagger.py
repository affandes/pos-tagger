# Class tagger
import kata

class Tagger():

    __kamus = False

    def __init__(self, kamus):
        self.__kamus = kamus

    def tag(self, term_list):
        terms = [kata.Kata(term, self.__kamus.get_tag(term)) for term in term_list]

        return [term.__str__() for term in terms]

