import svgwrite
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget

points = [(0, 90), (10, 14), (220, 31), (420, 37), (510, 33)]

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1100, 1100)
        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 1080, 1080)
        frame = svgwrite.Drawing(None, profile="tiny")
        frame.add(frame.polygon(points, fill="blue"))
        self.widgetSvg.load(bytes(frame.tostring(), encoding='utf8'))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
