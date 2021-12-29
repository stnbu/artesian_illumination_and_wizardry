import svgwrite, webbrowser, math
from sympy import Matrix

f = "/tmp/thing.svg"

import svgwrite 

path = [(100,100),(100,200),(200,200),(200,100)]

image = svgwrite.Drawing('test.svg',size=(300,300))

rectangle = image.add(image.polygon(path,id ='polygon',stroke="black",fill="white"))
rectangle.add(image.animateTransform("rotate","transform",id="polygon", from_="0 150 150", to="360 150 150",dur="4s",begin="0s",repeatCount="indefinite"))
text = image.add(image.text('rectangle1',insert=(150,30),id="text"))
text.add(image.animateColor("fill", attributeType="XML",from_="green", to="red",id="text", dur="4s",repeatCount="indefinite"))

image.save()

import sys; sys.exit()







drawing = svgwrite.Drawing(f, profile='tiny')

theta = math.pi / 2


def rotate(points, angle):
    result = []
    rotato = Matrix([
        [math.cos(angle), - math.sin(angle)],
        [math.sin(angle),   math.cos(angle)],
    ])
    for pair in points:
        thing = rotato * Matrix(pair)
        result.append((int(thing[0]), int(thing[1])))
    #print(result)
    return result

# drawing.add(
#     drawing.rect(
#         (10, 10),
#         (300, 200),
#         stroke=svgwrite.rgb(10, 10, 16, '%'),
#         fill='red'
#     )
# )

randoid_points = [(0, 90), (100, 140), (220, 310), (420, 370), (510, 330)]
    
drawing.add(
    drawing.polygon(randoid_points, fill='blue')
)

drawing.add(
    drawing.polygon(rotate(randoid_points, math.pi / 5), fill='green')
)

drawing.save()

#webbrowser.open('file://' + f, new=0, autoraise=True)
