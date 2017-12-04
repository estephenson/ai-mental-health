import spacy
import nltk.data
from textblob import TextBlob
import numpy as np
import csv
import itertools
zip = getattr(itertools, 'izip', zip)

file = open('CultureRelatedDiaognosticIssues.txt','r')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

a = []
names = []
sentiments = []
meanArr = []

for line in file:
    miniList = line.split("|")
    names.append(int(miniList[0].strip()))
    a.append(miniList[1].strip())
file.close()

nlp = spacy.load('en')
for i in range(len(a)):
    chap = a[i]
    chapSents = []
    sentences = tokenizer.tokenize(chap)
    for sentence in sentences:
        line = TextBlob(sentence)
        chapSents.append(line.sentiment.subjectivity)
    sentiments.append(chapSents)

for j in range(len(sentiments)):
    sentArray = sentiments[j]
    mean = np.mean(sentArray)
    meanArr.append(mean)

with open('subjectivityScores.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(names, meanArr))
f.close()

with open('chapterTextScore.csv', 'w') as f:
    



print()
print()
print()
