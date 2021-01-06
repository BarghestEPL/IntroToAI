import sys
import pygame as pg

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)


pg.init()
width, height = 800, 600
screen = pg.display.set_mode((width, height))
pg.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))

font = pg.font.SysFont("consolas", 18)


class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def is_in(self, p):
        w1 = self.a.x * (self.c.y - self.a.y) + (p.y - self.a.y) * (self.c.x - self.a.x) - p.x * (self.c.y - self.a.y)
        w1 /= (self.b.y - self.a.y) * (self.c.x - self.a.x) - (self.b.x - self.a.x) * (self.c.y - self.a.y)

        w2 = p.y - self.a.y - w1 * (self.b.y - self.a.y)
        w2 /= self.c.y - self.a.y

        text = font.render(f"w1: {round(w1, 2)}, w2: {round(w2, 2)}", True, WHITE)
        screen.blit(text, (50, 50))
        return w1 > 0 and w2 > 0 and (w1 + w2) < 1

    def draw(self):
        pg.draw.line(screen, WHITE, self.a, self.b)
        pg.draw.line(screen, WHITE, self.b, self.c)
        pg.draw.line(screen, WHITE, self.c, self.a)


e = pg.Vector2(100.0, 100.0)
f = pg.Vector2(700.0, 100.0)
g = pg.Vector2(400.0, 500.0)
triangle = Triangle(g, e, f)

fps = 60
fpsClock = pg.time.Clock()
while True:
    screen.fill((0, 0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Update
    m = pg.Vector2(pg.mouse.get_pos())

    # Draw.
    pg.draw.circle(screen, GREEN if triangle.is_in(m) else RED, m, 5)
    triangle.draw()

    pg.display.flip()
    fpsClock.tick(fps)
