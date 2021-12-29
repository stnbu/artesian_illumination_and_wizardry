import svgwrite
from PyQt5.QtCore import QFileSystemWatcher
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget

size = 30

points = [(0, 0), (size, 0), (size, size), (0, size)]

SVG_PATH = "/tmp/aiw.svg"

def path_to_bytes(path):
    return open(path, "rb").read()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.file_watcher = QFileSystemWatcher()
        self.file_watcher.fileChanged.connect(self.on_file_changed)
        self.file_watcher.addPaths([SVG_PATH])

        self.palette = QSvgWidget(parent=self)
        self.palette.setGeometry(10, 10, 1080, 1080)
        self.palette.load(path_to_bytes(SVG_PATH))

    def on_file_changed(self, path):
        self.palette.load(path_to_bytes(path))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
