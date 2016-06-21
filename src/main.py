#!/usr/bin/env python
# -*- codign: utf-8 -*-

import os
import xlwt as xlwt

from Frequency.IniParser import IniParser
from Frequency.FrequencyDict import FrequencyDict
from StarDict.StarDict import StarDict

ConfigFileName = "Setting.ini"


class Main:
    def __init__(self):
        self.listLanguageDict = []
        self.result = []

        try:
            config = IniParser(ConfigFileName)

            self.pathToBooks = config.GetValue("PathToBook")
            self.pathResult = config.GetValue("PathToResult")
            self.countWord = config.GetValue("CountWord")
            self.pathToWordNetDict = config.GetValue("PathToWordNetDict")
            self.pathToStarDict = config.GetValue("PathToStarDict")

            listPathToStarDict = [item.strip() for item in self.pathToStarDict.split(";")]

            for path in listPathToStarDict:
                languageDict = StarDict(path)
                self.listLanguageDict.append(languageDict)

            self.listBooks = self.__GetAllFiles(self.pathToBooks)

            self.frequencyDict = FrequencyDict(self.pathToWordNetDict)

            self.__Run()

        except Exception as e:
            print('Error: "%s"' % e)

    def __GetAllFiles(self, path):
        try:
            return [os.path.join(path, file) for file in os.listdir(path)]
        except Exception:
            raise Exception('Path "%s" does not exists' % path)

    def __GetTranslate(self, word):
        valueWord = ""
        for dict in self.listLanguageDict:
            valueWord = dict.Translate(word)
            if valueWord != "":
                return valueWord
        return valueWord

    def __SaveResultToExcel(self):
        try:
            if not os.path.exists(self.pathResult):
                raise Exception('No such directory: "%s"' % self.pathResult)
            if self.result:
                description = 'Frequency Dictionary'
                style = xlwt.easyxf('font: name Times New Roman')
                wb = xlwt.Workbook()
                ws = wb.add_sheet(description + ' ' + self.countWord)
                nRow = 0
                for item in self.result:
                    ws.write(nRow, 0, item[0], style)
                    ws.write(nRow, 1, item[1], style)
                    ws.write(nRow, 2, item[2], style)
                    nRow += 1
                wb.save(os.path.join(self.pathResult, description + '.xls'))
        except Exception as e:
            print(e)

    def __Run(self):
        for book in self.listBooks:
            self.frequencyDict.ParseBook(book)

        mostCommonElements = self.frequencyDict.FindMostCommonElements(self.countWord)

        for item in mostCommonElements:
            word = item[0]
            counterWord = item[1]
            valueWord = self.__GetTranslate(word)
            self.result.append([counterWord, word, valueWord])

        self.__SaveResultToExcel()


if __name__ == '__main__':
    main = Main()
