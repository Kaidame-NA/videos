from manim import *


class TestAnimation(Scene):
    def construct(self):
        star = Star(n=5, fill_color=RED, stroke_color=BLUE)
        circle = Circle(fill_color=DARK_BLUE, fill_opacity=0.8, stroke_color=BLUE)

        self.play(FadeIn(star, run_time=2))

        self.wait()

        self.play(Transform(star, circle))

        self.wait(0.5)

        self.play(FadeOut(circle))
