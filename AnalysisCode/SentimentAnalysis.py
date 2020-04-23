from matplotlib import pyplot as plt
from nltk import sentiment
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
from afinn import Afinn
import os
import re

testfilepath = "/users/andrei/documents/github/poemanalysis/poemscorpus/1900"
poems = []
poemNames = []
poemDict = {}
afinn = Afinn()
aScore = 0
SID = SentimentIntensityAnalyzer()
SIDScore = 0

for poem in os.listdir(testfilepath):
    if poem.endswith(".txt"):
        poemNames.append(poem[:-4].replace("_", " "))
        fopen = open(testfilepath + "/" + poem)
        poems.append(re.sub(r'[^\w\s]', '', fopen.read().lower().replace("\n", " ")))
        fopen.close()

for i in range(0, len(poems)):
    poemDict[poemNames[i]] = poems[i]
for poem in poemDict:
    line = tokenize.sent_tokenize(poemDict[poem])
    score = afinn.score(line[0])
    aScore += score
    ss = SID.polarity_scores(line[0])
    SIDScore += ss["compound"]
    print('\n')
    print(poem, '\n', score)
print('\n')
print("Compound Afinn Score: ", aScore)
print("Compound SID Score: ", SIDScore)
