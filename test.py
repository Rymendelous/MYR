from manim import *

class CreateRectangle(Scene):
    def construct(self):
        rectangle = Rectangle(width=3.0, height=4.5, color=WHITE)
        self.play(Create(rectangle))
        bar = Line(start=rectangle.get_corner(UL) + DOWN * 1, end=rectangle.get_corner(UR) + DOWN * 1, color=WHITE, stroke_width=6)
        self.play(Create(bar))
        self.play(AnimationGroup(bar.animate.shift(4 * LEFT), rectangle.animate.shift(4 * LEFT)), run_time=0.25)
        rectangle2 = Rectangle(width=3.0, height=4.5, color=WHITE)
        self.play(Create(rectangle2))
        bar2 = Line(start=rectangle2.get_corner(UL) + DOWN * 1, end=rectangle2.get_corner(UR) + DOWN * 1, color=WHITE, stroke_width=6)
        self.play(Create(bar2))
        self.play(AnimationGroup(bar2.animate.shift(4 * RIGHT), rectangle2.animate.shift(4 * RIGHT)), run_time=0.25)
        oval = Ellipse(width=3.0, height=2.0, color=WHITE)
        oval.move_to(ORIGIN)
        self.play(Create(oval))
        oval_bar = Line(start=oval.get_left() + UP * 0.15, end=oval.get_right() + UP * 0.15, color=WHITE, stroke_width=6)
        self.play(Create(oval_bar))