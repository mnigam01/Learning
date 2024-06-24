from enum import Enum
from abc import ABC, abstractmethod

class LogLevel(Enum):
    ERROR = 1
    INFO = 2
    DEBUG = 3

class LogProcessor(ABC):
    def __init__(self, next_processor=None) -> None:
        self.next_processor = next_processor

    def log(self,log_level:LogLevel, mssge:str):
        if self.next_processor:
            self.next_processor.log(log_level, mssge)
        else:
            raise Exception("can't fulfill this request")
    
class InfoLogProcessor(LogProcessor):
    def __init__(self, next_processor=None) -> None:
        super().__init__(next_processor)
    def log(self, log_level: LogLevel, mssge: str):
        if log_level.name=="INFO":
            print(mssge)
        else:
            super().log(log_level, mssge)

class DebugLogProcessor(LogProcessor):
    def __init__(self, next_processor=None) -> None:
        super().__init__(next_processor)
    def log(self, log_level: LogLevel, mssge: str):
        if log_level.name=="DEBUG":
            print(mssge)
        else:
            super().log(log_level, mssge)

class ErrorLogProcessor(LogProcessor):
    def __init__(self, next_processor=None) -> None:
        super().__init__(next_processor)
    def log(self, log_level: LogLevel, mssge: str):
        if log_level.name=="ERROR":
            print(mssge)
        else:
            super().log(log_level, mssge)

if __name__=="__main__":
    log_obj = InfoLogProcessor(DebugLogProcessor(ErrorLogProcessor()))
    log_obj.log(LogLevel.ERROR, "exception happened")
    log_obj.log(LogLevel.DEBUG, "need to debug this")
    log_obj.log(LogLevel.INFO, "just for info")