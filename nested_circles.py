window_dim = 500
num_children = 6
num_iterations = 5

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return "({x}, {y}), {r}".format(x=self.x, y=self.y, r=self.r)

def draw_circle(circle):
    x, y = circle.x, circle.y
    d = 2 * circle.r
    ellipse(x, y, d, d)

def get_children(circle, n):
    x, y = circle.x, circle.y
    sr = circle.r / 2
    a = 2 * PI / n
    children = []
    for i in range(n):
        dx = sr * cos(i*a)
        dy = sr * sin(i*a)
        child = Circle(x + dx, y + dy, sr)
        children.append(child)
    return children

def draw_circles(seed,  num_children=4, num_iterations=2):
    cur_gen_circles = [seed]
    for _ in range(num_iterations):
        next_gen_circles = []
        for circle in cur_gen_circles:
            draw_circle(circle)
            next_gen_circles += get_children(circle, num_children)
        cur_gen_circles = next_gen_circles

def setup():
    size(window_dim, window_dim)
    background(255)
    noFill()
    circle = Circle(window_dim / 2, window_dim / 2, window_dim / 2)
    draw_circles(circle, num_children, num_iterations)