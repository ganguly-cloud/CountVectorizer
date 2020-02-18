'''
What is vectorizer ? and why ?
--> The text must be parsed to remove words, called tokenization. Then the words need to
    be encoded as integers or floating point values for use as input to a machine
    learning algorithm, called feature extraction (or vectorization).

--> The scikit-learn library offers easy-to-use tools to perform both tokenization and
    feature extraction of your text data.
--> Its usually used to convert text formated data into int or float or machine readable format.
--> It can be performed by a simple command using "CountVectorizer"

'''

from sklearn.feature_extraction.text import CountVectorizer
corpus = ['This is the first document.',
'This document is the second document.',
'And this is the third 12 45one.',
'Is this the first document?',
]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
'''
[u'12', u'45one', u'and', u'document', u'first', u'is', u'second', u'the',
u'third', u'this'] '''
pri= X.toarray()

print pri
'''

[[0 0 0 1 1 1 0 1 0 1]
 [0 0 0 2 0 1 1 1 0 1]
 [1 1 1 0 0 1 0 1 1 1]
 [0 0 0 1 1 1 0 1 0 1]]  '''
