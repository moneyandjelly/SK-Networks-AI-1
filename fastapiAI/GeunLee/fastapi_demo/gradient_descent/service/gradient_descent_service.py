from abc import ABC, abstractmethod

class GradientDescentService(ABC):

    @abstractmethod
    def gradientDecentTrain(self):
        pass