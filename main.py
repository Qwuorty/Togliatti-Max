import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from draw_c import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QApplication

class Yellow(QDialog, Ui_Dialog):
    def init(self):
        super().init()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.toggle_drawing)
        self.drawing_enabled = False  # Флаг для отслеживания, нужно ли рисовать

    def toggle_drawing(self):
        self.drawing_enabled = True
        self.update()

    def paintEvent(self, event):
        self.qp = QPainter(self)
        if self.drawing_enabled:
            self.draw()
        self.qp.end()

    def draw(self):
        R = randint(20, 100)
        x = randint(0, self.width() - R)
        y = randint(0, self.height() - R)
        self.qp.setBrush(QColor(*[randint(0, 255) for _ in range(3)]))
        self.qp.drawEllipse(x, y, R, R)


if name == 'main':
    app = QApplication(sys.argv)
    ex = Yellow()
    ex.show()
    sys.exit(app.exec_())