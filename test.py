from manim import *

class CreateRectangle(Scene):
    def construct(self):
        # Premier rectangle
        rectangle = Rectangle(width=3.0, height=4.5, color=WHITE)
        self.play(Create(rectangle))

        # Texte "Oeuvre" plus haut et à gauche
        text = Text("Oeuvre").move_to(rectangle.get_center()).shift(UP * 2.7 + LEFT * 0.05 + DOWN * 0.9)  
        self.play(Write(text))

        # Ligne (barre) associée au premier rectangle
        bar = Line(
            start=rectangle.get_corner(UL) + DOWN * 1,
            end=rectangle.get_corner(UR) + DOWN * 1,
            color=WHITE,
            stroke_width=6
        )
        self.play(Create(bar))
        self.play(
            AnimationGroup(
                bar.animate.shift(4 * LEFT),
                rectangle.animate.shift(4 * LEFT),
                text.animate.shift(4 * LEFT)  # Déplacer également le texte
            ),
            run_time=0.25
        )

        # Deuxième rectangle
        rectangle2 = Rectangle(width=3.0, height=4.5, color=WHITE)
        self.play(Create(rectangle2))

        # Texte "Auteur" à droite du rectangle et lié à son mouvement
        text2 = Text("Auteur").move_to(rectangle.get_center()).shift(UP * 2.7 + RIGHT * 4 + DOWN * 0.9)
        self.play(Write(text2))

        # Ligne (barre) associée au deuxième rectangle
        bar2 = Line(
            start=rectangle2.get_corner(UL) + DOWN * 1,
            end=rectangle2.get_corner(UR) + DOWN * 1,
            color=WHITE,
            stroke_width=6
        )
        self.play(Create(bar2))
        self.play(
            AnimationGroup(
                bar2.animate.shift(4 * RIGHT),
                rectangle2.animate.shift(4 * RIGHT),
                text2.animate.shift(4 * RIGHT)  # Déplacer également le texte
            ),
            run_time=0.25
        )

        # Ellipse
        oval = Ellipse(width=3.0, height=2.0, color=WHITE)
        oval.move_to(ORIGIN)
        self.play(Create(oval))

        # Barre dans l'ellipse, reliant les deux rectangles
        oval_bar = Line(
            start=rectangle.get_corner(UR) + DOWN * 2.1,  # Coin supérieur droit du premier rectangle
            end=rectangle2.get_corner(UL) + DOWN * 2.1,  # Coin supérieur gauche du deuxième rectangle
            color=WHITE,
            stroke_width=6
        )
        self.play(Create(oval_bar))

        small_text = Text("a_écrit", font_size=30).move_to(oval.get_center() + UP*0.5)  # Taille réduite
        self.play(Write(small_text))
