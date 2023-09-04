""" TF-DF:  Program  uses the  Term Frequency Inverse Document Frequency (tf-idf) vectors to find the most similar pair of lines in a given data set. Solution is tested on other data sets.
"""

import math
import random
import numpy as np
import io
from io import StringIO
text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def main(text):
    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    docs = [line.lower().split() for line in text.split('\n')]
    N = len(docs)

    # 2. go over each unique word and calculate its term frequency, and its document frequency
    vocabulary = list(set(text.lower().split()))
    n = len(vocabulary)
    # print(vocabulary, n)   
    df = {}
    tf = {}
    for word in vocabulary:
        tf[word] = [doc.count(word)/len(doc) for doc in docs]
        df[word] = sum([word in doc for doc in docs])/N
    # print(tf, df)


    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector
    tfidf = np.zeros((N, n), dtype= np.float64)
    for doc_index, doc in enumerate(docs) :
        for word_index, word in enumerate(vocabulary):
            tfidf[doc_index,word_index] = tf[word][doc_index] * math.log(1/df[word] , 10)
    # print(tfidf)
    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.
    dist = np.empty((N, N), dtype= np.float64)
    for i, row1 in enumerate(tfidf):
        for j, row2 in enumerate(tfidf):
            if i == j:
                dist[i,j] = np.Inf
            else:
                dist[i, j] =  np.sum(abs(row1 - row2))
    print(np.unravel_index(np.argmin(dist), dist.shape))

main(text)

