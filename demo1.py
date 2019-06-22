import tagger.tagger as tg
import kamus.kamus as km
import nltk
import time
from nltk.tag.sequential import UnigramTagger

terms = ['adu','abang','caca','abi','acara']

nldict = UnigramTagger([[
    ('a','n'),
    ('abah','n'),
    ('abang','n'),
    ('abi','n'),
    ('abu','n'),
    ('acak','n'),
    ('acar','n'),
    ('acara','n'),
    ('ancam','n'),
]])

my_kamus = km.Kamus()
my_tagger = tg.Tagger(my_kamus)

startx = time.time()
my_result = my_tagger.tag(terms)
endx = time.time()


starty = time.time()
#nlresult = nldict.tag(terms)
endy = time.time()

#print(endx-startx)
#print(endy-starty)

my_kamus.update_kamus(('baru','a'))
my_kamus.update_kamus(('basa','a'))
my_kamus.update_kamus(('bata','n'))

#print my_result
#print "------------"
#print nlresult
my_kamus.save_kamus('simpan baru.txt')