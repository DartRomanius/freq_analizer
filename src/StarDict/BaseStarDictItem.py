#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class BaseStarDictItem:
    def __init__(self, pathToDict, exp):
        self.encoding = "utf-8"
        self.dictionaryFile = self.__PathToFileInDirByExp(pathToDict, exp)
        self.realFileSize = os.path.getsize(self.dictionaryFile)

    def __PathToFileInDirByExp(self, path, exp):
        if not os.path.exists(path):
            raise Exception('Path "%s" does not exists' % path)
        end = '.%s' % (exp)
        list = [f for f in os.listdir(path) if f.endswith(end)]
        if list:
            return os.path.join(path, list[0])
        else:
            raise Exception('File does not exist: "*.%s"' % exp)


if __name__ == '__main__':
    pass
