class Component:
    def operation(self) -> str:
        pass


class Text(Component):
    def operation(self) -> str:
        return "Text"


class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> str:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class BoldWeight(Decorator):
    def operation(self) -> str:
        return f"BoldWeight({self.component.operation()})"


class ItalicStyle(Decorator):
    def operation(self) -> str:
        return f"ItalicStyle({self.component.operation()})"


def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}", end="")


def main():
    text = Text()
    client_code(text)
    print("\n")

    decorator_bold = BoldWeight(text)
    decorator_italic = ItalicStyle(decorator_bold)
    client_code(decorator_italic)

if __name__ == "__main__":
    main()