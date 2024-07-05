from convolution_neural_network.repository.cnn_repository import ConvolutionNeralNetworkRepository

from tensorflow.keras import datasets

class ConvolutionNeuralNetworkRepositoryImpl(ConvolutionNeralNetworkRepository):
    def loadCifar10Data(self):
        print(f"repository -> loadCifar10Data()")

        return datasets.cifar10.load_data()