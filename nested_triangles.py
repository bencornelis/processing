d = 500
i = 5

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def midpoint(p, q):
    return Point((p.x + q.x) / 2, (p.y + q.y) / 2)

def get_children(t):
    m1 = midpoint(t.p1, t.p2)
    m2 = midpoint(t.p2, t.p3)
    m3 = midpoint(t.p3, t.p1)

    return [
        Triangle(t.p1, m1, m3),
        Triangle(m1, t.p2, m2),
        Triangle(m3, m2, t.p3),
        Triangle(m1, m2, m3),
    ]
    
def draw_triangles(seed, iterations=5):
    cur_gen = [seed]
    for _ in range(iterations):
        next_gen = []
        for t in cur_gen:
            draw_triangle(t)
            next_gen += get_children(t)
        cur_gen = next_gen

def draw_triangle(t):
    triangle(t.p1.x, t.p1.y, t.p2.x, t.p2.y, t.p3.x, t.p3.y)

def setup():
    size(d, d)
    background(255)
    noFill()
    p1 = Point(d/2, 0)
    p2 = Point(0, d)
    p3 = Point(d, d)
    t = Triangle(p1, p2, p3)
    draw_triangles(t, iterations=i)