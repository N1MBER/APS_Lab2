# Подключаемый полный или задний привод автомобиля
from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def info(self) -> str:
        pass


class Context:
    prop = property()

    def __init__(self, state: State) -> None:
        self._state = state

    @prop.getter
    def state(self) -> State:
        return self._state

    @prop.setter
    def state(self, state: State) -> None:
        self._state = state

    def print_state_status(self):
        print('State status: {}'.format(self._state.info()))


class FourWheelDrive(State):

    def info(self) -> str:
        return '4x4'


class RearDrive(State):

    def info(self) -> str:
        return 'Rear drive'


def main():
    context = Context(FourWheelDrive())
    context.print_state_status()

    context = Context(RearDrive())
    context.print_state_status()


if __name__ == '__main__':
    main()
