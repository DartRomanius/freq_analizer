#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""


import re
import os

from collections import Counter
from  WordNet.Lemmatizer import Lemmatizer


class FrequencyDict:
    def __init__(self, pathToWordNetDict):
        self.wordPattern = re.compile("((?:[a-zA-Z]+[-']?)*[a-zA-Z]+)")
        self.frequencyDict = Counter()
        self.lemmatizer = Lemmatizer(pathToWordNetDict)

    def ParseBook(self, file):
        if file.endswith(".txt"):
            self.__ParseTxtFile(file, self.__FindWordsFromContent)
        elif file.endswith(".pdf"):
            self.__ParsePdfFile(file, self.__FindWordsFromContent)
        else:
            print("Warning: The file format is not supported: '%s'" % file)

    def __ParsePdfFile(self, pdf_file, content_handler):
        pass

    def __ParseTxtFile(self, txt_file, content_handler):
        try:
            with open(txt_file, 'rU') as file:
                for line in file:
                    content_handler(line)
        except Exception as e:
            print("Error parsing '%s'" % txt_file, e)

    def __FindWordsFromContent(self, content):
        result = self.wordPattern.findall(content)
        for word in result:
            word = word.lower()
            self.frequencyDict[word] += 1

    def FindMostCommonElements(self, countWord):
        dict = list(self.frequencyDict.items())
        dict.sort(key=lambda t: t[0])
        dict.sort(key=lambda t: t[1], reverse=True)
        return dict[0:int(countWord)]


if __name__ == '__main__':
    pass
