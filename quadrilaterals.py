n = 10
WHITE = 255

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Quad:
    def __init__(self, p1, p2, p3, p4):
        # p1 ---- p2
        # |        |
        # |        |
        # |        |
        # p3 ---- p4
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        
def draw_quad(qd, col):
    s = createShape()
    s.beginShape()
    s.fill(col)
    s.noStroke()
    s.vertex(qd.p1.x, qd.p1.y)
    s.vertex(qd.p2.x, qd.p2.y)
    s.vertex(qd.p3.x, qd.p3.y)
    s.vertex(qd.p4.x, qd.p4.y)
    s.endShape(CLOSE)
    shape(s)

def midpoint(p, q):
    return Point((p.x + q.x) / 2, (p.y + q.y) / 2)

def get_inner_quad(qd):
    p1 = midpoint(qd.p1, qd.p2)
    p2 = midpoint(qd.p2, qd.p3)
    p3 = midpoint(qd.p3, qd.p4)
    p4 = midpoint(qd.p4, qd.p1)
    return Quad(p1, p2, p3, p4)

def draw_quads(seed, get_col, n=5):
    qd = seed
    for i in range(n):
        col = get_col(i, n)
        draw_quad(qd, col)
        qd = get_inner_quad(qd)

def setup():
    size(1000, 500)
    seed1 = Quad(
        Point(0, 0),
        Point(width / 2, 0),
        Point(width / 2, height),
        Point(0, height)
    )

    seed2 = Quad(
        Point(width / 2, 0),
        Point(width, 0),
        Point(width, height),
        Point(width / 2, height)
    )

    dark_to_light = lambda i, m: (WHITE / m) * i
    light_to_dark = lambda i, m: (WHITE / m) * (n - i)
    draw_quads(seed1, get_col=dark_to_light, n=n)
    draw_quads(seed2, get_col=light_to_dark, n=n)