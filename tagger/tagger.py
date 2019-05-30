# Class tagger
import tokenizer
import kata

class Tagger():

    __kamus = False
    __tokenizer = False

    def __init__(self, kamus):
        self.__kamus = kamus
        self.__tokenizer = tokenizer.Tokenizer()

    def tag(self, dokumen):
        term_list = self.__tokenizer.tokenize(dokumen)
        terms = [kata.Kata(term, self.__kamus.get_tag(term)) for term in term_list]

        return [term.__str__() for term in terms]

