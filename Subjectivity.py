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
labels = ['Intellectual Disability (Intellectual Developmental Disorder)','Autism Spectrum Disorder','Attention-Deficit/Hyperactivity Disorder','Specific Learning Disorder'
,'Developmental Coordination Disorder'
,'Stereotypic Movement Disorder'
,'Tic Disorders'
,'Delusional Disorder'
,'Brief Psychotic Disorder'
,'Schizoaffective Disorder'
,'Schizophrenia'
,'Bipolar I Disorder'
,'Bipolar and Related Disorder Due to Another Medical Condition'
,'Major Depressive Disorder'
,'Premenstrual Dysphoric Disorder'
,'Separation Anxiety Disorder'
,'Selective Mutism'
,'Specific Phobia'
,'Social Anxiety Disorder (Social Phobia)'
,'Panic Disorder'
,'Panic Attack Specifier'
,'Generalized Anxiety Disorder'
,'Obsessive-Compulsive Disorder'
,'Body Dysmorphic Disorder'
,'Hoarding Disorder'
,'Trichotillomania (Hair-Pulling Disorder)'
,'Reactive Attachment Disorder'
,'Posttraumatic Stress Disorder'
,'Acute Stress Disorder'
,'Adjustment Disorders'
,'Dissociative Identity Disorder'
,'Dissociative Amnesia'
,'Depersonalization/Derealization Disorder'
,'Somatic Symptom Disorder'
,'Illness Anxiety Disorder'
,'Conversion Disorder (Functional Neurological Symptom Disorder)'
,'Psychological Factors Affecting Other Medical Conditions'
,'Pica'
,'Avoidant/Restrictive Food Intake Disorder'
,'Anorexia Nervosa'
,'Bulimia Nervosa'
,'Binge-Eating Disorder'
,'Enuresis'
,'Narcolepsy'
,'Obstructive Sleep Apnea Hypopnea'
,'Circadian Rhythm Sleep-Wake Disorders'
,'Nightmare Disorder'
,'Substance/Medication-Induced Sleep Disorder'
,'Delayed Ejaculation'
,'Erectile Disorder'
,'Female Orgasmic Disorder'
,'Female Sexual Interest/Arousal Disorder'
,'Genito-Pelvic Pain/Penetration Disorder'
,'Male Hypoactive Sexual Desire Disorder'
,'Premature (Early) Ejaculation'
,'Substance/Medication-Induced Sexual Dysfunction'
,'Gender Dysphoria'
,'Oppositional Defiant Disorder'
,'Intermittent Explosive Disorder'
,'Conduct Disorder'
,'Alcohol Use Disorder'
,'Alcohol Intoxication'
,'Caffeine Withdrawal'
,'Cannabis Use Disorder'
,'Phencyclidine Use Disorder'
,'Other Hallucinogen Use Disorder'
,'Inhalant Use Disorder'
,'Opioid Use Disorder'
,'Sedative, Hypnotic, or Anxiolytic Use Disorder'
,'Stimulant Use Disorder'
,'Tobacco Use Disorder'
,'Other (or Unknown) Substance  Use Disorder'
,'Other (or Unknown) Substance Withdrawal'
,'Gambling Disorder'
,'Mild Neurocognitive Disorder'
,'Major or Mild Neurocognitive Disorder Due to Alzheimer_Ñés Disease'
,'General Personality Disorder'
,'Paranoid Personality Disorder'
,'Schizoid Personality Disorder'
,'Antisocial Personality Disorder'
,'Schizoid Personality Disorder'
,'Borderline Personality Disorder'
,'Histrionic Personality Disorder'
,'Avoidant Personality Disorder'
,'Dependent Personality Disorder'
,'Obsessive-Compulsive Personality Disorder'
,'Fetishistic Disorder']

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

with open('jsonData.json', 'w') as outfile:
     json.dump([{'title': label, 'chapter': text, 'sentiment scores': sentiments} for label, text, sentiments in zip(labels, sentenceArr, sentiments)], outfile, sort_keys = True, indent = 4,
               ensure_ascii = False)

print()
