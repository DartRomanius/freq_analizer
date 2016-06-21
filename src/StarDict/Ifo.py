#!/usr/bin/env python
# -*- coding: utf-8 -*-


from StarDict.BaseStarDictItem import BaseStarDictItem
from Frequency.IniParser import IniParser


class Ifo(BaseStarDictItem):
    def __init__(self, pathToDict):
        BaseStarDictItem.__init__(self, pathToDict, 'ifo')

        self.iniParser = IniParser(self.dictionaryFile)

        self.bookName = self.__getParameterValue("bookname", None)
        self.wordCount = self.__getParameterValue("wordcount", None)
        self.synWordCount = self.__getParameterValue("synwordcount", "")
        self.idxFileSize = self.__getParameterValue("idxfilesize", None)
        self.idxOffsetBits = self.__getParameterValue("idxoffsetbits", 32)
        self.author = self.__getParameterValue("author", "")
        self.email = self.__getParameterValue("email", "")
        self.description = self.__getParameterValue("description", "")
        self.date = self.__getParameterValue("date", "")
        self.sameTypeSequence = self.__getParameterValue("sametypesequence", None)
        self.dictType = self.__getParameterValue("dicttype", "")

    def __getParameterValue(self, key, defaultValue):
        try:
            return self.iniParser.GetValue(key)
        except:
            if defaultValue is not None:
                return defaultValue
            raise Exception('\n"%s" has invalid format (missing parameter: "%s")' % (self.dictionaryFile, key))


if __name__ == '__main__':
    pass
