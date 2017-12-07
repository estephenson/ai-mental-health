import csv
import sys
from textblob import TextBlob
import spacy
import numpy as np
import matplotlib.pyplot as plt
import nltk.data
import mpld3

file = open('CultureRelatedDiaognosticIssues.txt','r')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

searchWord = sys.argv[1]
a = []
names=[]
nameSet = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
freq = [7,4,2,2,7,4,4,3,4,5,1,5,8,1,3,14,2,10,1]
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
    newChaps.append('#4DB6AC')

for i in range(len(names)):
    for j in range(len(chapters)):
        if (i == chapters[j]):
            newChaps[i] = '#283593'


fig, ax = plt.subplots(subplot_kw=dict(axisbg='white'))

scatter = ax.scatter(range(len(names)), meanArr, color=newChaps)
title = "Diagnoses that contain the word: " + searchWord
ax.set_title(title, fontsize=20)
ax.set_xlabel("Diagnosis", fontsize=15)
ax.set_ylabel("Subjectivity Score", fontsize=15)

tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
mpld3.plugins.connect(fig, tooltip)
mpld3.show()
