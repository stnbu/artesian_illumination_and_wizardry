import svgwrite, webbrowser, math, os
from sympy import Matrix
from PyQt5.QtCore import QByteArray
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget

def get_rotate_matrix(angle):
    return Matrix(
        [
            [math.cos(angle), -math.sin(angle)],
            [math.sin(angle), math.cos(angle)],
        ]
    )

points = [(0, 90), (100, 140), (220, 310), (420, 370), (510, 330)]

num_frames = 90
total_angle = math.pi / 4
angle_delta = num_frames / num_frames
delta_rotate_matrix = get_rotate_matrix(angle_delta)

#os.makedirs("build", exist_ok=True)

for index in range(0, num_frames):
    continue  # pass
    frame = svgwrite.Drawing("build/xframe_%04d.svg" % index, profile="tiny")
    frame.add(frame.polygon(points, fill="blue"))
    frame.save()
    for jndex, point in enumerate(points):
        point = delta_rotate_matrix * Matrix(point)
        points[jndex] = [int(c) for c in point]

from xml.etree import ElementTree

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1100, 1100)
        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 1080, 1080)
        self.frame = svgwrite.Drawing("/tmp/xyzzz2.svg")
        xml = self.frame.tostring()
        xml = QByteArray(bytes(xml, encoding='utf8'))
        self.widgetSvg.load(xml)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


##################
# path = [(100, 100), (100, 200), (200, 200), (200, 100)]
# image = svgwrite.Drawing("test.svg", size=(300, 300))
# rectangle = image.add(image.polygon(path, id="polygon", stroke="black", fill="white"))
# rectangle.add(
#     image.animateTransform(
#         "rotate",
#         "transform",
#         id="polygon",
#         from_="0 150 150",
#         to="360 150 150",
#         dur="4s",
#         begin="0s",
#         repeatCount="indefinite",
#     )
# )
# text = image.add(image.text("rectangle1", insert=(150, 30), id="text"))
# text.add(
#     image.animateColor(
#         "fill",
#         attributeType="XML",
#         from_="green",
#         to="red",
#         id="text",
#         dur="4s",
#         repeatCount="indefinite",
#     )
# )
