from manimlib import *

class TaylorSeriesSinDerivation(Scene):
    def construct(self):
        # Part 1: Intro to Taylor Series
        intro_title = Text("Taylor Series Expansion", font="Consolas", font_size=48)
        self.play(Write(intro_title), run_time=1)
        self.wait(1)

        intro_description = Tex(
            "A method to approximate functions using polynomials",
            font_size=36
        )
        self.play(Transform(intro_title, intro_description), run_time=1)
        self.wait(1)
        self.play(FadeOut(intro_title))

        # Part 2: Taylor Series Formula
        taylor_series_formula = Tex(
            "f(x) = f(a) + f'(a)(x-a) + \\frac{f''(a)}{2!}(x-a)^2 + \\frac{f'''(a)}{3!}(x-a)^3 + \\cdots",
            font_size=36
        )
        self.play(FadeInFrom(taylor_series_formula, LEFT), run_time=1.5)
        self.wait(1)
        self.play(FadeOutAndShift(taylor_series_formula, RIGHT))

        # Part 3: Applying to sin(x)
        sinx_text = Text("Applying to f(x) = sin(x)", font="Consolas", font_size=48)
        self.play(FadeInFrom(sinx_text, LEFT), run_time=1.5)
        self.wait(1)
        self.play(FadeOutAndShift(sinx_text, RIGHT))

        # Part 4: Display derivatives of sin(x)
        derivatives = [
            "f(x) = \\sin(x)",
            "f'(x) = \\cos(x)",
            "f''(x) = -\\sin(x)",
            "f'''(x) = -\\cos(x)",
            "f^{(4)}(x) = \\sin(x)"
        ]
        derivatives_group = VGroup(*[Tex(d, font_size=36) for d in derivatives])
        derivatives_group.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(FadeInFrom(derivatives_group, LEFT), run_time=1.5)
        self.wait(1)
        self.play(FadeOutAndShift(derivatives_group, RIGHT))

        # Part 5: Values at x = 0
        values_at_zero = [
            "\\sin(0) = 0",
            "\\cos(0) = 1",
            "-\\sin(0) = 0",
            "-\\cos(0) = -1",
            "\\sin(0) = 0"
        ]
        values_group = VGroup(*[Tex(v, font_size=36) for v in values_at_zero])
        values_group.arrange(DOWN, aligned_edge=RIGHT, buff=0.5)
        self.play(FadeInFrom(values_group, LEFT), run_time=1.5)
        self.wait(1)
        self.play(FadeOutAndShift(values_group, RIGHT))

        # Part 6: Taylor series expansion of sin(x)
        taylor_series_sinx = Tex(
            "\\sin(x) = x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + \\frac{x^9}{9!} - \\cdots",
            font_size=36
        )
        self.play(FadeInFrom(taylor_series_sinx, LEFT), run_time=1.5)
        self.wait(2)

# This line ensures that your script runs successfully
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = f"manim -pql {module_name} TaylorSeriesSinDerivation"
    os.system(command_A)
