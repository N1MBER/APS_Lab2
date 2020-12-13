from abc import abstractmethod, ABC


class SmallCar(ABC):

    @abstractmethod
    def get_car_model(self):
        pass

    @abstractmethod
    def get_car_category(self):
        pass


class MediumCar(ABC):

    @abstractmethod
    def get_car_model(self):
        pass

    @abstractmethod
    def get_car_category(self):
        pass


class BigCar(ABC):

    @abstractmethod
    def get_car_model(self):
        pass

    @abstractmethod
    def get_car_category(self):
        pass


class BMWSmallCar(SmallCar):
    def get_car_model(self):
        print("It's a BMW")

    def get_car_category(self):
        print("It's a small car")


class BMWMediumCar(MediumCar):
    def get_car_model(self):
        print("It's a BMW")

    def get_car_category(self):
        print("It's a medium car")


class BMWBigCar(BigCar):
    def get_car_model(self):
        print("It's a BMW")

    def get_car_category(self):
        print("It's a big car")


class AudiSmallCar(SmallCar):
    def get_car_model(self):
        print("It's a Audi")

    def get_car_category(self):
        print("It's a small car")


class AudiMediumCar(MediumCar):
    def get_car_model(self):
        print("It's a Audi")

    def get_car_category(self):
        print("It's a medium car")


class AudiBigCar(BigCar):
    def get_car_model(self):
        print("It's a Audi")

    def get_car_category(self):
        print("It's a big car")


class BenzSmallCar(SmallCar):
    def get_car_model(self):
        print("It's a Mercedes Benz")

    def get_car_category(self):
        print("It's a small car")


class BenzMediumCar(MediumCar):
    def get_car_model(self):
        print("It's a Mercedes Benz")

    def get_car_category(self):
        print("It's a medium car")


class BenzBigCar(BigCar):
    def get_car_model(self):
        print("It's a Mercedes Benz")

    def get_car_category(self):
        print("It's a big car")


class ModelFactory(ABC):

    @abstractmethod
    def create_small_car(self) -> SmallCar:
        pass

    @abstractmethod
    def create_medium_car(self) -> MediumCar:
        pass

    @abstractmethod
    def create_big_car(self) -> BigCar:
        pass


class BMWModelFactory(ModelFactory):
    def create_small_car(self) -> SmallCar:
        return BMWSmallCar()

    def create_medium_car(self) -> MediumCar:
        return BMWMediumCar()

    def create_big_car(self) -> BigCar:
        return BMWBigCar()


class AudiModelFactory(ModelFactory):
    def create_small_car(self) -> SmallCar:
        return AudiSmallCar()

    def create_medium_car(self) -> MediumCar:
        return AudiMediumCar()

    def create_big_car(self) -> BigCar:
        return AudiBigCar()


class BenzModelFactory(ModelFactory):

    def create_small_car(self) -> SmallCar:
        return BenzSmallCar()

    def create_medium_car(self) -> MediumCar:
        return BenzMediumCar()

    def create_big_car(self) -> BigCar:
        return BenzBigCar()


def create_car(model_factory: ModelFactory):
    small_car = model_factory.create_small_car()
    medium_car = model_factory.create_medium_car()
    big_car = model_factory.create_big_car()

    small_car.get_car_category()
    small_car.get_car_model()
    medium_car.get_car_category()
    medium_car.get_car_model()
    big_car.get_car_category()
    big_car.get_car_model()


def main():
    create_car(BMWModelFactory())
    create_car(AudiModelFactory())
    create_car(BenzModelFactory())


if __name__ == '__main__':
    main()
