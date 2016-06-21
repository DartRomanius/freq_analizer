#!/usr/bin/env python
# -*- coding: utf-8 -*-


from WordNet.BaseWordNetItem import BaseWordNetItem


class WordNetAdjective(BaseWordNetItem):
    def __init__(self, pathToWordNetDict):
        BaseWordNetItem.__init__(self, pathToWordNetDict, 'adj.exc', 'index.adj')

        self.rule = (
            ["er", ""],
            ["er", "e"],
            ["est", ""],
            ["est", "e"]
        )


if __name__ == '__main__':
    pass
