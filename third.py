import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Design(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('Нажми меня!', self)
        self.btn.move(220, 30)
        self.show()


class MyEllipse:
    def __init__(self, x, y, d, randcol):
        self.x, self.y, self.d = x, y, d
        self.randcol = randcol

    def draw(self, qp):
        qp.setPen(QColor(self.randcol[0], self.randcol[1], self.randcol[2]))
        qp.setBrush(QColor(self.randcol[0], self.randcol[1], self.randcol[2]))
        qp.drawEllipse(self.x, self.y, self.d, self.d)


class MyWidget(QMainWindow, Design):
    def __init__(self):
        super().__init__()
        self.btn.clicked.connect(self.draw)
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
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        randcol = (r, g, b)
        self.objects.append(MyEllipse(x, y, d, randcol))
        self.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())