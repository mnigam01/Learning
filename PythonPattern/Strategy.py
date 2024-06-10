"""
change different strategy or algorithm based on need like we can go with normal drive or advance drive
"""
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def implement_strategy(self):
        pass

class MeanAverage(Strategy):
    def implement_strategy(self):
        return "mean is implemented"

class Median(Strategy):
    def implement_strategy(self):
        return "median is implemented"

class Chart:
    def __init__(self, strategy) -> None:
        self._strategy = strategy
    def paint(self):
        return self._strategy.implement_strategy()

if __name__ == "__main__":
    obj = Chart(MeanAverage())
    print(obj.paint())
        
