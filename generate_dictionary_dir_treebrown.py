import nltk
import kamus.kamus as km

tuple_of_brown = nltk.corpus.brown.tagged_words()
tuple_of_treebank = nltk.corpus.treebank.tagged_words()

my_kamus = km.Kamus()

for tupl in tuple_of_brown:
    my_kamus.update_kamus(tupl)


for tupl in tuple_of_treebank:
    my_kamus.update_kamus(tupl)


my_kamus.save_kamus_dir('output/treebrown')