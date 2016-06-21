#!/usr/bin/env python
# -*- coding: utf-8 -*-

from WordNet.WordNetAdverb import WordNetAdverb
from WordNet.WordNetNoun import WordNetNoun
from WordNet.WordNetVerb import WordNetVerb
from WordNet.WordNetAdjective import WordNetAdjective


class Lemmatizer:
    def __init__(self, pathToWordNetDict):
        self.splitter = "-"
        # initializing
        adj = WordNetAdjective(pathToWordNetDict)
        noun = WordNetNoun(pathToWordNetDict)
        adverb = WordNetAdverb(pathToWordNetDict)
        verb = WordNetVerb(pathToWordNetDict)
        self.wordNet = [verb, noun, adj, adverb]

    def GetLemma(self, word):
        wordArr = word.split(self.splitter)
        resultWord = []
        for word in wordArr:
            lemma = self.__GetLemmaWord(word)
            if lemma is not None:
                resultWord.append(lemma)
        if resultWord is not None:
            return self.splitter.join(resultWord)
        return None

    def __GetLemmaWord(self, word):
        for item in self.wordNet:
            lemma = item.GetLemma(word)
            if lemma is not None:
                return lemma
        return None


if __name__ == '__main__':
    pass
