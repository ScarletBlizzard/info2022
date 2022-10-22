import pygame
from vec2d import Vec2d


class Polyline:

    def __init__(self, surface, steps=35, points=None, speeds=None):
        self.surface = surface
        self.steps = steps

        if points is None:
            self.points = []
        else:
            self.points = points

        if speeds is None:
            self.speeds = []
        else:
            self.speeds = speeds

    def add_point(self, point, speed):
        self.points.append(point)
        self.speeds.append(speed)

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].x > self.surface.get_width() or self.points[p].x < 0:
                self.speeds[p] = Vec2d(-self.speeds[p].x, self.speeds[p].y)
            if self.points[p].y > self.surface.get_height() or self.points[p].y < 0:
                self.speeds[p] = Vec2d(self.speeds[p].x, -self.speeds[p].y)

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек и линий на экране"""
        if style == "line":
            knot = Knot(self.surface).get_knot(self.points, self.steps)
            for p_n in range(-1, len(knot)-1):
                pygame.draw.line(self.surface, color,
                                 knot[p_n].int_pair(),
                                 knot[p_n+1].int_pair(), width)
        elif style == "points":
            for p in self.points:
                pygame.draw.circle(self.surface, color, p.int_pair(), width)

    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg]*alpha + self.get_point(points, alpha, deg-1)*(1-alpha)

    def get_points(self, base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))
        return res

class Knot(Polyline):
    def get_knot(self, points, count):
        if len(points) < 3:
            return []
        res = []
        for i in range(-2, len(points) - 2):
            ptn = []
            ptn.append((points[i]+points[i+1]) * 0.5)
            ptn.append(points[i+1])
            ptn.append((points[i+1]+points[i+2]) * 0.5)

            res.extend(self.get_points(ptn, count))
        return res

