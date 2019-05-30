# Class Tokenizer
import re


class Tokenizer:
    __pattern = r'''(?x)
    ...          ([A-Z]\.)+
    ...         |\d+:\d+
    ...         |(https?://)?(\w+\.)(\w{2,})+([\w/]+)?
    ...         |[@\#]?\w+(?:[-']\w+)*
    ...         |\$\d+(\.\d+)?%?
    ...         |\\[Uu]\w+
    ...         |\.\.\.
    ...         |[!?]+
    ...     '''

    __pattrn = r"http[s]?://[\w\_\-\.]+.[\w]{2,}[\/\?]{1}[\w\_\-\.\&\=]+" \
               r"|\w+" \
               r"|[!?]+" \
               r"|[@\#]?\w+(?:[-']\w+)*"

    def __init__(self, pattern=''):
        if len(pattern) > 1:
            self.__pattern = pattern

    def tokenize(self, teks):
        return re.findall(self.__pattrn, teks)
