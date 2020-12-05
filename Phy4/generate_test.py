from unittest import TestCase, main
from unittest.mock import patch
from generate import WindowsDialog
from generate import WebDialog
from generate import WindowsButton
from generate import HTMLButton


class AbstractFactoryTestCase(TestCase):

    # проверка верной отрисовки диалога на Windows с разрешением 2560x1600
    # функцию get_res делаем Mock-объектом,
    # т.к. нам важно проверить, чтобы правильно отрисовывалось окно при определенном разрешении,
    # а не логику функции нахождения разрешения
    @patch('generate.get_res', return_value="2560x1600")
    def test_win_window_hr(self, get_res):
        dialog = WindowsDialog()
        self.assertEqual("Создание и отрисовка Windows диалога с разрешением 2560x1600",
                         dialog.paint(get_res("platform")))

    # проверка верной отрисовки диалога на Windows с разрешением 1600x1200
    # функцию get_res делаем Mock-объектом аналогично прошлому тесту
    @patch('generate.get_res', return_value="1600x1200")
    def test_win_window_mr(self, get_res):
        dialog = WindowsDialog()
        self.assertEqual("Создание и отрисовка Windows диалога с разрешением 1600x1200",
                         dialog.paint(get_res("platform")))

    # проверка верной отрисовки диалога на Windows с разрешением 1280x1024
    # функцию get_res делаем Mock-объектом аналогично прошлым тестам
    @patch('generate.get_res', return_value="1280x1024")
    def test_win_window_lr(self, get_res):
        dialog = WindowsDialog()
        self.assertEqual("Создание и отрисовка Windows диалога с разрешением 1280x1024",
                         dialog.paint(get_res("platform")))

    def test_win_render(self):
        dialog = WindowsDialog()
        self.assertEqual("Диалог запустился с Windows кнопка и Windows textbox", dialog.render())

    def test_web_render(self):
        dialog = WebDialog()
        self.assertEqual("Диалог запустился с HTML кнопка и HTML textbox", dialog.render())

    def test_win_button(self):
        dialog = WindowsDialog()
        button = dialog.create_button()
        self.assertEqual("Windows кнопка", button.operation())

    def test_win_text(self):
        dialog = WindowsDialog()
        button = dialog.create_button()
        self.assertEqual("Windows кнопка", button.operation())

    def test_web_button(self):
        dialog = WebDialog()
        button = dialog.create_button()
        self.assertEqual("HTML кнопка", button.operation())

    def test_web_text(self):
        dialog = WebDialog()
        button = dialog.create_button()
        self.assertEqual("HTML кнопка", button.operation())

    # проверка верной отрисовки диалога на Web с разрешением 2560x1600
    # функцию get_res делаем Mock-объектом,
    # т.к. нам важно проверить, чтобы правильно отрисовывалось окно при определенном разрешении,
    # а не логику функции нахождения разрешения
    @patch('generate.get_res', return_value="2560x1600")
    def test_web_window_hr(self, get_res):
        dialog = WebDialog()
        self.assertEqual("Создание и отрисовка Web диалога с разрешением 2560x1600",
                         dialog.paint(get_res("platform")))

    # проверка верной отрисовки диалога на Web с разрешением 1600x1200
    # функцию get_res делаем Mock-объектом аналогично прошлому тесту
    @patch('generate.get_res', return_value="1600x1200")
    def test_web_window_mr(self, get_res):
        dialog = WebDialog()
        self.assertEqual("Создание и отрисовка Web диалога с разрешением 1600x1200",
                         dialog.paint(get_res("platform")))

    # проверка верной отрисовки диалога на Web с разрешением 1280x1024
    # функцию get_res делаем Mock-объектом аналогично прошлым тестам
    @patch('generate.get_res', return_value="1280x1024")
    def test_web_window_lr(self, get_res):
        dialog = WebDialog()
        self.assertEqual("Создание и отрисовка Web диалога с разрешением 1280x1024",
                         dialog.paint(get_res("platform")))


if __name__ == '__main__':
    main()