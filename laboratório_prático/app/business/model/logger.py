from abc import ABC, abstractmethod
import datetime

class Logger(ABC):
    def __init__(self):
        self.__log_str = f"Log from {datetime.datetime.now().strftime("%d/%m/%Y_%H:%M:%S")}"

    def logToFile(self):
        self.convert2Format()

    @abstractmethod
    def convert2Format(self) -> None:
        pass

    def saveFile(self, path):
        with open(path, "w") as f:
            



class PDFLogger(Logger):
