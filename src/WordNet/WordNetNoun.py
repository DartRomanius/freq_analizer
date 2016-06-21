#!/usr/bin/env python
# -*- coding: utf-8 -*-

from WordNet.BaseWordNetItem import BaseWordNetItem


class WordNetNoun(BaseWordNetItem):
    def __init__(self, pathToWordNetDict):
        BaseWordNetItem.__init__(self, pathToWordNetDict, 'noun.exc', 'index.noun')

        self.rule = (
            ["s", ""],
            ["'s", ""],
            ["'", ""],
            ["ses", "s"],
            ["xes", "x"],
            ["zes", "z"],
            ["ches", "ch"],
            ["shes", "sh"],
            ["men", "man"],
            ["ies", "y"]
        )

    def GetLemma(self, word):
        word = word.strip().lower()

        if len(word) <= 2:
            return None

        if word.endswith("ss"):
            return None

        lemma = self._GetDictValue(self.cacheWords, word)
        if lemma is not None:
            return lemma

        if self._IsDefined(word):
            return word

        lemma = self._GetDictValue(self.wordNetExcDict, word)
        if lemma is not None:
            return lemma

        suff = ""
        if word.endswith("ful"):
            word = word[:-3]
            suff = "ful"

        lemma = self._RuleNormalization(word)
        if lemma is not None:
            lemma += suff
            self.cacheWords[word] = lemma
            return lemma

        return None


if __name__ == '__main__':
    pass
