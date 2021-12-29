import svgwrite
from PyQt5.QtCore import QFileSystemWatcher
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget

size = 30

points = [(0, 0), (size, 0), (size, size), (0, size)]

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.file_watcher = QFileSystemWatcher()
        self.file_watcher.fileChanged.connect(self.on_file_changed)
        self.file_watcher.addPaths(["/tmp/aiw.svg"])

        self.palette = QSvgWidget(parent=self)
        self.palette.setGeometry(10, 10, 1080, 1080)

        frame = svgwrite.Drawing(None)
        frame.add(frame.polygon(points, fill="blue"))

        self.palette.load(bytes(frame.tostring(), encoding='utf8'))

    def on_file_changed(self, path):
        print(("---------------------------\n"
              "I changed!!! -->\n"
              "  str(%s)\n"
              "  type(%s)\n"
              "  repr(%s)\n\n") % (path, type(path), repr(path)))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
