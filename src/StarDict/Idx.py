#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack
from StarDict.BaseStarDictItem import BaseStarDictItem


class Idx(BaseStarDictItem):
    def __init__(self, pathToDict, wordCount, idxFileSize, idxOffsetBits):
        BaseStarDictItem.__init__(self, pathToDict, 'idx')

        self.idxDict = {}
        self.idxFileSize = int(idxFileSize)
        self.idxOffsetBits = int(idxOffsetBits / 8)
        self.wordCount = int(wordCount)

        self.__CheckRealFileSize()

        self.__FillIdxDict()

        self.__CheckRealWordCount()

    def __CheckRealFileSize(self):
        if self.realFileSize != self.idxFileSize:
            raise Exception('size of the "%s" is incorrect' % self.dictionaryFile)

    def __CheckRealWordCount(self):
        realWordCount = len(self.idxDict)
        if realWordCount != self.wordCount:
            raise Exception('word count of the "%s" is incorrect' % self.dictionaryFile)

    def __getIntFromByteArray(self, sizeInt, stream):
        byteArray = stream.read(sizeInt)

        formatCharacter = 'L'
        if sizeInt == 8:
            formatCharacter = 'Q'
        format = '>' + formatCharacter

        integer =  (unpack(format, byteArray))[0]
        return int(integer)

    def __FillIdxDict(self):
        languageWord = ""
        with open(self.dictionaryFile, 'rb') as stream:
            while True:
                byte = stream.read(1)
                if not byte:
                    break
                if byte != b'\0':
                    languageWord += byte.decode("utf-8")
                else:
                    wordDataOffset = self.__getIntFromByteArray(self.idxOffsetBits, stream)
                    wordDataSize = self.__getIntFromByteArray(4, stream)

                    self.idxDict[languageWord] = [wordDataOffset, wordDataSize]
                    languageWord = ""

    def GetLocationWord(self, word):
        try:
            return self.idxDict[word]
        except KeyError:
            return [None, None]


if __name__ == '__main__':
    pass
