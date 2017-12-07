import spacy
import nltk.data
from textblob import TextBlob
import numpy as np
import csv
import itertools
import json

zip = getattr(itertools, 'izip', zip)
data = {}
file = open('CultureRelatedDiaognosticIssues.txt','r')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

a = []
names = []
sentiments = []
meanArr = []
sentenceArr = []

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
    sentenceArr.append(sentences)
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

with open('subjectivityScorebySentence.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(sentenceArr, sentiments))
f.close()

json_data = json.dumps([{'chapter': text, 'sentiment scores': sentiments} for text, sentiments in zip(sentenceArr, sentiments)])
with open('jsonData.json', 'w') as outfile:
     json.dump([{'chapter': text, 'sentiment scores': sentiments} for text, sentiments in zip(sentenceArr, sentiments)], outfile, sort_keys = True, indent = 4,
               ensure_ascii = False)

print(json_data)
print(len(sentiments))
print()
