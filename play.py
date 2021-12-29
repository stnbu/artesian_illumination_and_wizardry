import svgwrite
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget

size = 30

points = [(0, 0), (size, 0), (size, size), (0, size)]

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.palette = QSvgWidget(parent=self)
        self.palette.setGeometry(10, 10, 1080, 1080)
        frame = svgwrite.Drawing(None)
        frame.add(frame.polygon(points, fill="blue"))
        self.palette.load(bytes(frame.tostring(), encoding='utf8'))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
