import svgwrite, webbrowser, math, os
from PyQt5.QtCore import QByteArray
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget

points = [(0, 90), (10, 14), (220, 31), (420, 37), (510, 33)]

circle = b"""
<svg height="100" width="100">
  <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
  Sorry, your browser does not support inline SVG.
</svg>
"""

my_blob = b"""
<svg height="100%" width="100%">
<polygon fill="blue" points="0,90 10,14 22,31 42,37 51,33" />
</svg>
"""

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1100, 1100)
        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 1080, 1080)

        frame = svgwrite.Drawing("/tmp/aiw.svg", profile="tiny")
        frame.add(frame.polygon(points, fill="blue"))
        xxx = bytes(frame.tostring(), encoding='utf8')

        self.widgetSvg.load(xxx)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
