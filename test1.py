from manimlib import *

class ChainRuleVisualization(Scene):
    def construct(self):
        # Basic Number line for x
        number_line_x = NumberLine()
        number_line_x.shift(2 * UP)  # Position the number line above the center

        # Basic Number line for x^2
        number_line_x2 = NumberLine()
        number_line_x2.shift(2 * DOWN)  # Position the number line below the center

        # Labels for the number lines
        label_x = Tex("x").set_color(BLUE).next_to(number_line_x, LEFT)
        label_x2 = Tex("x^2").set_color(BLUE).next_to(number_line_x2, LEFT)

        # Add everything to the scene
        self.add(number_line_x, label_x, number_line_x2, label_x2)
        self.wait()
