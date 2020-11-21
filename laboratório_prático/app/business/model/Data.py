from datetime import datetime, date


class Data:
    def __init__(self, dmy):
        self.__dmy = dmy

    def getDMY(self):
        return self.__dmy
    
    def setDMY(self, dmy):
        self.__dmy = dmy

    def converteData (self, dmy):
        return dmy