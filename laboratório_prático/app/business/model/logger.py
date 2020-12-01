from abc import ABC, abstractmethod
import datetime
import json

class Logger(ABC):
    def __init__(self):
        self.__data = {"datetime": datetime.datetime.now().strftime("%d/%m/%Y_%H:%M:%S"), "users_accesses": []}

    def logToFile(self):
        self.convert2Format()

    def writeAcess(self, user_name):
        self.__data["users_accesses"].append({"username": user_name, "acess_time": datetime.datetime.now().strftime("%d/%m/%Y_%H:%M:%S")})

    @abstractmethod
    def convert2Format(self) -> None:
        pass

    def saveFile(self, path):
        with open(path, "w") as f:
            f.write(self.convert2Format())

        f.close()



class PDFLogger(Logger):
    def convert2Format(self):
        return json.dump()

class HTMLLogger(Logger):
    