import svgwrite, webbrowser, math, os
from PyQt5.QtCore import QByteArray
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget

points = [(0, 90), (100, 140), (220, 310), (420, 370), (510, 330)]

circle = b"""
<svg height="100" width="100">
  <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
  Sorry, your browser does not support inline SVG.
</svg>
"""

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1100, 1100)
        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 1080, 1080)

        # self.frame = svgwrite.Drawing("/tmp/aiw.svg", profile="tiny")
        # self.frame.add(self.frame.polygon(points, fill="blue"))
        # xml = self.frame.tostring()
        # self.xml = QByteArray(bytes(xml, encoding='utf8'))

        self.widgetSvg.load(circle)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
