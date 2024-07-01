from gradient_descent.repository.gradient_descent_repository_impl import GradientDescentRepositoryImpl
from gradient_descent.service.gradient_descent_service import GradientDescentService



class GradientDescentServiceImpl(GradientDescentService):

    def __init__(self):
        self.gradientDecentRepository = GradientDescentRepositoryImpl()
    def gradientDecentTrain(self):
        print("service -> gradientDecentTrain()")

        X, y = self.gradientDecentRepository.createTrainData()
        print(f"X: {X}")
        print(f"y: {y}")
