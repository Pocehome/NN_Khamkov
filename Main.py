import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyEllipse:
    def __init__(self, x, y, d):
        self.x, self.y, self.d = x, y, d

    def draw(self, qp):
        qp.setPen(QColor(255, 255, 0))
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(self.x, self.y, self.d, self.d)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw)

        self.qp = QPainter()
        self.objects = []

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        for obj in self.objects:
            obj.draw(self.qp)
        self.qp.end()

    def draw(self):
        x = randint(50, 400)
        y = randint(50, 400)
        d = randint(10, 100)
        self.objects.append(MyEllipse(x, y, d))
        self.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())