import tagger.tagger as tg
import kamus.kamus as km
import nltk
import time

terms = nltk.corpus.gutenberg.words("austen-emma.txt")

my_kamus = km.Kamus()
my_tagger = tg.Tagger(my_kamus)

startx = time.time()
my_tagger.tag(terms)
endx = time.time()


starty = time.time()
nltk.pos_tag(terms)
endy = time.time()

print(endx-startx)
print(endy-starty)