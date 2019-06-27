import nltk
import kamus.kamus as km
import tagger.tagger as tg

# load data gutenberg
words = nltk.corpus.gutenberg.words('austen-emma.txt')

# setup tagger
my_kamus = km.Kamus()
pos = tg.Tagger(my_kamus)

result = pos.tag(words)