from matplotlib import pyplot as plt
from nltk import sentiment
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
from afinn import Afinn
import os
import re

class SentimentAnalysis():
    def __init__(self):
        self.testfilepath = "/users/andrei/documents/github/poemanalysis/poemscorpus/1900"
        self.poems = []
        self.poemNames = []
        self.poemDict = {}
        self.afinn = Afinn()
        self.aScore = 0
        self.SID = SentimentIntensityAnalyzer()
        self.SIDScore = 0

    def openPoems(self):
        for poem in os.listdir(self.testfilepath):
            if poem.endswith(".txt"):
                self.poemNames.append(poem[:-4].replace("_", " "))
                fopen = open(self.testfilepath + "/" + poem)
                self.poems.append(re.sub(r'[^\w\s]', '', fopen.read().lower().replace("\n", " ")))
                fopen.close()


    def poemsToDict(self):
        for i in range(0, len(self.poems)):
            self.poemDict[self.poemNames[i]] = self.poems[i]


    def tokenizePoems(self):
        for poem in self.poemDict:
            line = tokenize.sent_tokenize(self.poemDict[poem])
            print(line)
            self.poemDict[poem] = line


SA = SentimentAnalysis()
SA.openPoems()
SA.poemsToDict()
SA.tokenizePoems()
"""
    score = afinn.score(line[0])
    aScore += score
    ss = SID.polarity_scores(line[0])
    SIDScore += ss["compound"]
    print('\n')
    print(poem, '\n', score)
print('\n')
print("Compound Afinn Score: ", aScore)
print("Compound SID Score: ", SIDScore)
"""
