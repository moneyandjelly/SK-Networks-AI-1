from abc import ABC, abstractmethod

class ConvolutionNeralNetworkRepository(ABC):

    @abstractmethod
    def loadCifar10Data(self):
        pass