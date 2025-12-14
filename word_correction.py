
'''
Code By: Tajender Singh Katal
Exploring textblob library 
'''
#import TextBlob library
from textblob import TextBlob,Word

# Spelling Correction 

# Method 1
incorrect = TextBlob("I am not in denger. I am the dyangr.")
correct= incorrect.correct()
print(correct)
#Output : I am not in danger. I am the danger.

# Method 2
word1 = Word('Neumonia')
print(word1.spellcheck())
# Output : [('Pneumonia', 1.0)] -- 1.0 is the confidence score 

word2 = Word('Suprem')
print(word2.spellcheck())
# Output : [('Supreme', 1.0)] -- 1.0 is the confidence score 

failWord1 = Word('Stocklom')
print(failWord1.spellcheck())
# Output : [('Stocklom', 0.0)] -- 0.0 is the confidence score

failWord2 = Word('Guci')
print(failWord2.spellcheck())
# Output : [('Such', 0.6453932584269663), ('Much', 0.30157303370786515), ('Luck', 0.012584269662921348), ('Duct', 0.009887640449438202), 
#           ('Foci', 0.007640449438202248), ('Duc', 0.004943820224719101), ('Qui', 0.0035955056179775282), ('Lui', 0.0017977528089887641), 
#           ('Lucy', 0.0017977528089887641), ('Duck', 0.0017977528089887641), ('Suck', 0.001348314606741573), ('Muco', 0.001348314606741573), 
#           ('Tuck', 0.0008988764044943821), ('Lucid', 0.0008988764044943821), ('Ici', 0.0008988764044943821), ('Buck', 0.0008988764044943821), 
#           ('Yuri', 0.00044943820224719103), ('Oui', 0.00044943820224719103), ('Mucin', 0.00044943820224719103), ('Lucia', 0.00044943820224719103), 
#           ('Guai', 0.00044943820224719103), ('Fuck', 0.00044943820224719103)] -- Multiple confidence score
print(failWord2.spellcheck()[0])
# Output : ('Such', 0.6453932584269663) -- 0.6453932584269663 is the confidence score

'''
NOTE:

TextBlob is good for:
common words, verbs, nouns, adjectives, grammar-like text

TextBlob is bad at:
names, cities, brands, technical terms, domain-specific vocabulary
'''