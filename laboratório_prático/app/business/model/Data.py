from datetime import datetime, date


class Data:
    def __init__(self, dmy):
        self.__dmy = dmy

    def getDMY(self):
        return self.__dmy
    
    def setDMY(self):
        return self.__dmy

    def converteData (self, dmy):
        return datetime.strptime(dmy, "%d/%m/%Y")