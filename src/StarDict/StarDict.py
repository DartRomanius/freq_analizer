#!/usr/bin/env python
# -*- coding: utf-8 -*-

from StarDict.Ifo import Ifo
from StarDict.Idx import Idx
from StarDict.Dict import Dict


class StarDict:
    def __init__(self, pathToDict):
        try:
            self.Ifo = Ifo(pathToDict)

            self.Idx = Idx(pathToDict, self.Ifo.wordCount, self.Ifo.idxFileSize, self.Ifo.idxOffsetBits)

            self.Dict = Dict(pathToDict, self.Ifo.sameTypeSequence)

        except Exception as e:
            print('Dictionary "%s" was not loaded: %s' % (pathToDict, e))

    def Translate(self, word):
        word = word.lower().strip()
        wordDataOffset, wordDataSize = self.Idx.GetLocationWord(word)

        if wordDataOffset == "" or wordDataSize == "":
            return None

        return self.Dict.GetTranslation(wordDataOffset, wordDataSize)


if __name__ == '__main__':
    pass
