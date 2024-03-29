import os
import re
import random


filedir = "/users/andrei/documents/github/poemanalysis/poemscorpus"
timePeriods = {}
fileMCs = {}

for f in os.listdir(filedir):
    if f != '.DS_Store':
        poemFolder = filedir + "/" + f
        timePeriods[f] = []
        for p in os.listdir(poemFolder):
            poemFile = poemFolder + '/' + p
            timePeriods[f].append(poemFile)


class MarkovChain():

    def __init__(self, filename, order):
        self.words = []
        self.order = order
        self.create(filename)


    def create(self, filename):
        self.a = {}
        self.prev=['_']*self.order
        openfile = open(filename)
        cleanfile=re.sub(r'[^\w\s]', '', openfile.read().lower().replace("\n", " ")).split()
        self.words = cleanfile


        for i in range(0, len(self.words)):
            prevTuple=tuple(self.prev)
            if prevTuple not in self.a:
                self.a[prevTuple] = {}
            self.a[prevTuple][self.words[i]] = self.a[prevTuple].get(self.words[i], 0) + 1
            self.prev.append(self.words[i])
            self.prev = self.prev[1:]
        prevTuple=tuple(self.prev)
        if prevTuple not in self.a:
            for i in range(0, self.order):
                prevTuple=tuple(self.prev)
                self.a[prevTuple] = {}
                self.a[prevTuple][self.words[i]] = self.a[prevTuple].get(self.words[i], 0) + 1
                self.prev.append(self.words[i])
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

    def discrete_prob(self, d):
        r = random.random()
        sum = 0
        for k in d:
            sum += d[k]
            if r < sum:
                return k

    def generate(self, mc, sep):
        current = list(random.choice(list(mc.keys())))
        seq = []
        for i in range(100):
            seq.append(self.discrete_prob(mc[tuple(current)]))
            current = current[1:] + [seq[-1]]
        return sep.join(seq)


def chainFilesSeparate(order):
    for periods in timePeriods:
        fileMCs[periods] = []
        for period in timePeriods[periods]:
            fileMCs[periods].append(MarkovChain(period, order))
    for chains in fileMCs:
        print(chains)
        for chain in fileMCs[chains]:
            print(chain.generate(chain.a, " "))
            print('\n')

chainFilesSeparate(4)
