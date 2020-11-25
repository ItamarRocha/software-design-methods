from datetime import datetime, date


class Data:
    def __init__(self, dmy):
        self.__d = dmy[:2]
        self.__m = dmy[3:5]
        self.__a = dmy[6:]
        self.__dmy = dmy

    def getDMY(self):
        return self.__dmy
    
    def setDMY(self, dmy):
        self.__dmy = dmy

    def converteData (self, dmy):
        return dmy