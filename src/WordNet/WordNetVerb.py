#!/usr/bin/env python
# -*- coding: utf-8 -*-


from WordNet.BaseWordNetItem import BaseWordNetItem


class WordNetVerb(BaseWordNetItem):
    def __init__(self, pathToWordNetDict):
        BaseWordNetItem.__init__(self, pathToWordNetDict, 'verb.exc', 'index.verb')

        self.rule = (
            ["s", ""],
            ["ies", "y"],
            ["es", "e"],
            ["es", ""],
            ["ed", "e"],
            ["ed", ""],
            ["ing", "e"],
            ["ing", ""]
        )


if __name__ == '__main__':
    pass
