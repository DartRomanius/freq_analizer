#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class BaseWordNetItem:
    def __init__(self, pathWordNetDict, excFile, indexFile):
        self.rule = ()

        self.wordNetExcDict = {}
        self.wordNetIndexDict = []

        self.excFile = os.path.join(pathWordNetDict, excFile)
        self.indexFile = os.path.join(pathWordNetDict, indexFile)

        self.__ParseFile(self.excFile, self.__AppendExcDict)
        self.__ParseFile(self.indexFile, self.__AppendIndexDict)

        self.cacheWords = {}

    def __AppendExcDict(self, line):
        group = [item.strip() for item in line.replace("\n", "").split(" ")]
        self.wordNetExcDict[group[0]] = group[1]

    def __AppendIndexDict(self, line):
        group = [item.strip() for item in line.split(" ")]
        self.wordNetIndexDict.append(group[0])

    def __ParseFile(self, file, contentHandler):
        try:
            with open(file, 'r') as openFile:
                for line in openFile:
                    contentHandler(line)
        except Exception as e:
            raise Exception('File does not load: "%s"' % file)

    def _GetDictValue(self, dict, key):
        try:
            return dict[key]
        except KeyError:
            return None

    def _IsDefined(self, word):
        if word in self.wordNetIndexDict:
            return True
        return False

    def GetLemma(self, word):
        word = word.strip().lower()

        if word is None:
            return None

        lemma = self._GetDictValue(self.cacheWords, word)
        if lemma is not None:
            return lemma

        if self._IsDefined(word):
            return word

        lemma = self._GetDictValue(self.wordNetExcDict, word)
        if lemma is not None:
            return lemma

        lemma = self._RuleNormalization(word)
        if lemma is not None:
            self.cacheWords[word] = lemma
            return lemma

        return None

    def _RuleNormalization(self, word):
        for replGroup in self.rule:
            endWord = replGroup[0]
            if word.endswith(endWord):
                lemma = word
                lemma = lemma.rstrip(endWord)
                lemma += replGroup[1]
                if self._IsDefined(lemma):
                    return lemma
        return None


if __name__ == '__main__':
    pass
