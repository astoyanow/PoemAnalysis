import nltk
import os
import re

class MarkovChain():

    def __init__(self, filename):
        self.words = []
        self.create(filename)


    def create(self, filename):
        self.a = {}
        self.prev=['_']
        openfile = open(filename)
        cleanfile=re.sub(r'[^\w\s]', '', openfile.read().lower().replace("\n", " ")).split()
        self.words = cleanfile


        for i in range(0, len(self.words)):
            prevTuple=tuple(self.prev)
            if prevTuple not in self.a:
                self.a[prevTuple] = {}
            self.a[prevTuple][self.words[i]] = self.a[prevTuple].get(self.words[i], 0) + 1
            print(prevTuple)
            self.prev.append(self.words[i])
            print(self.prev)
            self.prev = self.prev[1:]

        for k in self.a:
            sum1 = 0
            for k2 in self.a[k]:
                sum1 += self.a[k][k2]
            for k2 in self.a[k]:
                self.a[k][k2] /= sum1

        return self.a

    def probability(self, phrase):
        p = 1
        phrase=phrase.strip().lower()
        currentChar=''
        nextChar=''
        for char in range(0,len(phrase)-1):
            currentChar=tuple(phrase[char])
            nextChar=phrase[char+1]
            p*=self.a[currentChar].get(nextChar)
        return p

testfile = '/users/andrei/documents/github/poemanalysis/poemscorpus/a country wife.txt'
mc = MarkovChain(testfile)
print(mc.a)
print(mc.words)
for key in mc.a:
    print(key)
