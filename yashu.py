import nltk
nltk.download('wordnet')
from nltk.stem import wordnetlematizer
wnl=wordnetlematizer()
words=['runs','kings','gamings','flights']
for word in words:
    print(word+'__>'+wnl_lematize(word))


     




















  
