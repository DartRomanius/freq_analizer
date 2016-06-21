#!/usr/byn/env python
# -*- coding: utf-8 -*-

from StarDict.BaseStarDictItem import BaseStarDictItem

# Маркер может быть составным (к примеру, sametypesequence = tm).
# Виды одно-символьныx идентификаторов  словарных статей (для всех строчных идентификаторов текст в формате utf-8,
# заканчивается '\0'):
# 'm' - просто текст в кодировке utf-8, заканчивается '\0'
# 'l' - просто текст в НЕ в кодировке utf-8, заканчивается '\0'
# 'g' - текст размечен с помощью языка разметки текста Pango
# 't' - транскрипция в кодировке utf-8, заканчивается '\0'
# 'x' - текст в кодировке utf-8, размечен с помощью xdxf
# 'y' - текст в кодировке utf-8, содержит китайские(YinBiao) или японские (KANA) символы
# 'k' - текст в кодировке utf-8, размечен с помощью  KingSoft PowerWord XML
# 'w' - текст размечен с помощью  MediaWiki
# 'h' - текст размечен с помощью  Html
# 'n' - текст размечен формате для WordNet
# 'r' - текст содержит список ресурсов. Ресурсами могут быть файлы картинки (jpg), звуковые (wav), видео (avi),
#       вложенные(bin) файлы и др.
# 'W' - wav файл
# 'P' - картинка
# 'X' - этот тип зарезервирован для экспериментальных расширен


class Dict(BaseStarDictItem):
    def __init__(self, pathToDict, sameTypeSequence):
        BaseStarDictItem.__init__(self, pathToDict, 'dict')

        self.sameTypeSequence = sameTypeSequence

    def GetTranslation(self, wordDataOffset, wordDataSize):
        try:
            self.__CheckValidArgument(wordDataOffset, wordDataSize)

            with open(self.dictionaryFile, 'rb') as file:
                file.seek(wordDataOffset)
                byteArray = file.read(wordDataSize)
                return byteArray.decode(self.encoding)

        except Exception:
            return None

    def __CheckValidArgument(self, wordDataOffset, wordDataSize):
        if wordDataOffset is None:
            pass
        if wordDataOffset < 0:
            pass
        endDataSize = wordDataOffset + wordDataSize
        if wordDataOffset < 0 or wordDataSize < 0 or endDataSize > self.realFileSize:
            raise Exception


if __name__ == '__main__':
    pass
