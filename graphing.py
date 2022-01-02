import math, os, svgwrite

scale = 500
NEW_ORIGIN = scale, scale

def C(x, y):
    dx, dy = NEW_ORIGIN
    return dx + x, dy - y

frame = svgwrite.Drawing("foo2.svg")

frame.defs.add(frame.style('* {font-size: 9px;}'))

for i in range(0, 20):
    t = scale - ((scale/10) * i)
    if t == 0:
        continue

    text_x, text_y = C(3, -11)
    frame.add(frame.line(start=C(-scale, t), end=C(scale, t), stroke='lightgrey', stroke_width=1))
    frame.add(frame.circle(C(t, 0), 1, fill='black', stroke='black'))
    frame.add(frame.text("%d" % (t//50), x=[text_x + t], y=[text_y], fill='black'))

    frame.add(frame.line(start=C(t, scale), end=C(t, -scale), stroke='lightgrey', stroke_width=1))
    frame.add(frame.circle(C(0, t), 1, fill='black', stroke='black'))
    frame.add(frame.text("%d" % (t//50), x=[text_x], y=[text_y + t], fill='black'))

frame.add(frame.line(start=C(-scale, 0), end=C(scale, 0), stroke='red', stroke_width=1))
frame.add(frame.line(start=C(0, scale), end=C(0, -scale), stroke='red', stroke_width=1))
frame.add(frame.circle(C(0, 0), 1, fill='black', stroke='black'))

frame.save()
