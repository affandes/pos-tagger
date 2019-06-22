from collections import defaultdict
from nltk.tag.sequential import UnigramTagger
import nltk

terms = nltk.corpus.gutenberg.words("austen-emma.txt")
kamus = defaultdict(str)

kamus['a'] = 'z'
kamus['abah'] = 'n'
kamus['abang'] = 'n'
kamus['abi'] = 'n'
kamus['abu'] = 'n'
kamus['acak'] = 'v'
kamus['acar'] = 'n'
kamus['acara'] = 'n'
kamus['ancam'] = 'v'

pos = UnigramTagger([kamus.items()])

res = pos.tag(terms)

print res