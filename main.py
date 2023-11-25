import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5 import uic
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Загрузка интерфейса из файла UI.ui
        uic.loadUi('UI.ui', self)

        # Создание кнопки
        self.button = QPushButton('Нажми меня', self)
        self.button.clicked.connect(self.on_button_click)

        # Создание виджета для отображения окружностей
        self.circle_widget = CircleWidget()

        # Расположение компонентов на форме
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.circle_widget)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_button_click(self):
        # При нажатии кнопки добавляем случайную окружность на виджет
        diameter = random.randint(10, 100)
        self.circle_widget.add_circle(diameter)


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            painter.setBrush(QColor(255, 255, 0))  # желтый цвет
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])

    def add_circle(self, diameter):
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
