#!/usr/bin/env python
# -*- coding: utf-8 -*-

from WordNet.BaseWordNetItem import BaseWordNetItem


class WordNetAdverb(BaseWordNetItem):
    def __init__(self, pathToWordNetDict):
        BaseWordNetItem.__init__(self, pathToWordNetDict, 'adv.exc', 'index.adv')


if __name__ == '__main__':
    pass
