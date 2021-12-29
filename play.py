import svgwrite, webbrowser, math, os
from PyQt5.QtCore import QByteArray
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget

points = [(0, 90), (100, 140), (220, 310), (420, 370), (510, 330)]

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1100, 1100)
        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 1080, 1080)

        self.frame = svgwrite.Drawing("/tmp/aiw.svg", profile="tiny")
        self.frame.add(self.frame.polygon(points, fill="blue"))

        xml = self.frame.tostring()
        self.xml = QByteArray(bytes(xml, encoding='utf8'))
        self.widgetSvg.load(self.xml)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
