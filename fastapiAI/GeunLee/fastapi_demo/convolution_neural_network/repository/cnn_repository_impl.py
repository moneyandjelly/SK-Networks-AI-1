import numpy as np

from convolution_neural_network.repository.cnn_repository import ConvolutionNeralNetworkRepository

from tensorflow.keras import datasets

class ConvolutionNeuralNetworkRepositoryImpl(ConvolutionNeralNetworkRepository):
    def loadCifar10Data(self):
        print(f"repository -> loadCifar10Data()")

        return datasets.cifar10.load_data()

    def filteringClasses(self, imageList, labelList, targetClassList):
        filterMask = np.isin(labelList, targetClassList).flatten()
        filteredImageList = imageList[filterMask]
        filteredLabelList = labelList[filterMask]

        print(f"filteredImageList: {filteredImageList}, length: {len(filteredImageList)}")
        print(f"filteredImageList: {filteredLabelList}, length: {len(filteredLabelList)}")

        for index, classIndex in enumerate(targetClassList):
            filteredLabelList[filteredLabelList == classIndex] = index

        print(f"filteredLabelList: {filteredLabelList}, length: {len(filteredLabelList)}")
