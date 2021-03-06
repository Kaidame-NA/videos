from manim import *
import numpy as np

class TestAnimation(Scene):
    def construct(self):
        star = Star(n=5, fill_color=RED, stroke_color=BLUE)
        circle = Circle(fill_color=DARK_BLUE, fill_opacity=0.8, stroke_color=BLUE)

        self.play(FadeIn(star, run_time=2))

        self.wait()

        self.play(Transform(star, circle))

        self.wait(0.5)

        self.play(FadeOut(circle))


class CoordinateTest(Scene):
    def construct(self):
        dot = Dot(radius=0.16, color="#00AEFF")
        square = Square().shift(2 * LEFT)
        triangle = Triangle().shift(2 * RIGHT)
        circle = Circle().shift(2 * DOWN)
        star = Star(n=7).shift(2 * UP)

        self.add(dot, square, triangle, circle, star)

class MovementAnimation(Scene):
    def construct(self):
        dot = Dot(radius = 0.16, color = "#AE00FF")
        self.play(Create(dot))
        self.play(dot.animate.shift(2 * RIGHT))
        self.play(dot.animate.set_color("#00AEFF"))

class TextAnimate(Scene):
    def construct(self):
        text=Tex(r"Hello World", font_size=144)
        self.play(Write(text))

        self.add(text)
