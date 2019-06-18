import tagger.tagger as tg
import kamus.kamus as km

dok = 'Kita buat konsepnya ??? mirip Medium, hanya !!! 5aja !? topiknya f0kus ?!! pada dunia informatika. Dengan harapan dapat membantu kawan-kawan mahasiswa dan penggiat di bidang informatika http://www.guru99.com/python-regular-expressions-complete-tutorial.html #hashtag dan @mention ini'

my_kamus = km.Kamus()
my_tagger = tg.Tagger(my_kamus)

print my_tagger.tag(dok)
