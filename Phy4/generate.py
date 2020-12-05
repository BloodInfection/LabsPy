from __future__ import annotations
from abc import ABC, abstractmethod


def get_res(platform):
    if platform == "Настольный ПК":
        return "2560x1600"
    elif platform == "Ноутбук":
        return "1600x1200"
    elif platform == "Нетбук":
        return "1280x1024"


class Dialog(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_textbox(self):
        pass

    @abstractmethod
    def paint(self, resolution):
        pass

    def render(self) -> str:
        # Вызываем фабричный метод, чтобы получить объект-продукт.
        button = self.create_button()

        textbox = self.create_textbox()

        # Далее, работаем с этим продуктом.
        print(f"Создание и отрисовка {button.operation()}")
        print(f"Создание и отрисовка {textbox.operation()}")
        result = f"Диалог запустился с {button.operation()} и {textbox.operation()}"

        return result
 

class WindowsDialog(Dialog):
    def paint(self, resolution):
        return f"Создание и отрисовка Windows диалога с разрешением {resolution}"

    def create_button(self) -> Button:
        return WindowsButton()

    def create_textbox(self) -> Textbox:
        return WindowsTextbox()


class WebDialog(Dialog):
    def paint(self, resolution):
        return f"Создание и отрисовка Web диалога с разрешением {resolution}"

    def create_button(self) -> Button:
        return HTMLButton()

    def create_textbox(self) -> Textbox:
        return HTMLTextbox()


class Button(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class Textbox(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class WindowsButton(Button):
    def operation(self) -> str:
        return "Windows кнопка"


class HTMLButton(Button):
    def operation(self) -> str:
        return "HTML кнопка"


class WindowsTextbox(Textbox):
    def operation(self) -> str:
        return "Windows textbox"


class HTMLTextbox(Textbox):
    def operation(self) -> str:
        return "HTML textbox"


def client_code(creator: Dialog) -> None:
    print(creator.paint(get_res("Настольный ПК")), end="\n")
    print(creator.render(), end="")
    print("\n")
    print(creator.paint(get_res("Ноутбук")), end="\n")
    print(creator.render(), end="")
    print("\n")
    print(creator.paint(get_res("Нетбук")), end="\n")
    print(creator.render(), end="\n")
    print("\n")


if __name__ == "__main__":
    print("КЛИЕНТСКИЙ КОД WINDOWS ДИАЛОГА")
    client_code(WindowsDialog())
    print("\n")

    print("КЛИЕНТСКИЙ КОД WEB ДИАЛОГА")
    client_code(WebDialog())