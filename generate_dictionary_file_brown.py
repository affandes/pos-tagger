import nltk
import kamus.kamus as km

tuple_of_words = nltk.corpus.brown.tagged_words()

my_kamus = km.Kamus()

for tupl in tuple_of_words:
    my_kamus.update_kamus(tupl)


my_kamus.save_kamus('output/brown.csv')