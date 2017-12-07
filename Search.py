import csv
import sys
from textblob import TextBlob
import spacy
import numpy as np
import matplotlib.pyplot as plt
import nltk.data

file = open('CultureRelatedDiaognosticIssues.txt','r')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

searchWord = sys.argv[1]
a = []
names=[]
nameSet = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
freq = [7,4,2,2,7,4,4,3,4,5,1,5,8,1,3,14,2,10,1]
sentiments=[]
meanArr=[]

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

chapters = []
for i in range(len(a)):
    diagnosis = a[i]
    match = diagnosis.find(searchWord)
    if (match > -1):
        chapters.append(i)

print(chapters)

newChaps = []
for k in range(len(names)):
    newChaps.append('green')

for i in range(len(names)):
    for j in range(len(chapters)):
        if (i == chapters[j]):
            newChaps[i] = 'blue'

plt.bar(range(len(names)), meanArr, color=newChaps)
plt.show()
