

'''

Python program that outputs a list of all n-grams(one, two, three, and four) 
represented as string and its probability.

'''
from nltk import word_tokenize
from nltk.util import ngrams

file_content = open("in2.txt").read()
wordlist = word_tokenize(file_content)

listlen = len(wordlist)
for i in range(0,5):
    print('\n',i,'_Grams:\n')
    gramslist=ngrams(wordlist,i)
    for gram in gramslist:
        print(gram)
    prob = i/listlen
    print(prob)
