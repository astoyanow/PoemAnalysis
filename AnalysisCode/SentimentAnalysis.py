from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
from afinn import Afinn
import os
import re

class SentimentAnalysis():
    def __init__(self, period):
        self.period = period
        self.testfilepath = f"/users/andrei/documents/github/poemanalysis/poemscorpus/{self.period}"
        self.poems = []
        self.poemNames = []
        self.poemDict = {}
        self.afinn = Afinn()
        self.aCompScore = 0
        self.afinnDict = {}
        self.SID = SentimentIntensityAnalyzer()
        self.SIDCompScore = 0
        self.SIDDict = {}

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
            self.poemDict[poem] = line[0]


    def poemAfinn(self):
        for poem in self.poemDict:
            score = self.afinn.score(self.poemDict[poem])
            self.afinnDict[poem] = score
            self.aCompScore += score


    def poemSID(self):
        for poem in self.poemDict:
            ss = self.SID.polarity_scores(self.poemDict[poem])
            self.SIDDict[poem] = ss["compound"]
            self.SIDCompScore += ss["compound"]

SA = SentimentAnalysis('1900')
SA.openPoems()
SA.poemsToDict()
SA.tokenizePoems()
print(SA.poemDict)
SA.poemAfinn()
SA.poemSID()
print("Compound Afinn Score: ", SA.aCompScore)
print("Compound SID Score: ", SA.SIDCompScore)
print(SA.SIDDict, '\n')
print(SA.afinnDict)
