from abc import ABC, abstractmethod
import datetime
import json

class Logger(ABC):
    def __init__(self):
        self.__data = {"datetime": datetime.datetime.now().strftime("%d/%m/%Y_%H:%M:%S"), "users_accesses": []}
        self.__format = ".bin"

    def logToFile(self):
        self.convert2Format()

    def writeAcess(self, user_name):
        self.__data["users_accesses"].append({"username": user_name, "acess_time": datetime.datetime.now().strftime("%d/%m/%Y_%H:%M:%S")})

    @abstractmethod
    def convert2Format(self) -> None:
        pass

    def saveFile(self):
        with open(f"{self.__data['datetime']}.{self.__format}", "w") as f:
            f.write(self.convert2Format())

        f.close()

class JSONLogger(Logger):
    def __init__(self):
        Logger.__init__(self)
        self.__format = ".json"

    def convert2Format(self):
        return json.dumps(self.__data)

class TXTLogger(Logger):
    def __init__(self):
        Logger.__init__(self)
        self.__format = ".txt"

    def convert2Format(self):
        txt = f"---==== Log from {self.__data['datetime']} ====---\n\n"

        txt += "\tusername\t\tacess_time\n\n"

        for user in self.__data["users_accesses"]:
            txt += f"{user['username']}\t\t{user['acess_time']}\n"

        return txt

class CSVLogger(Logger):
    def __init__(self):
        Logger.__init__(self)
        self.__format = ".csv"

    def convert2Format(self):
        csv = "username,acess_time\n"

        for user in self.__data["users_accesses"]:
            csv += f"{user['username']},{user['acess_time']}\n"

        return csv