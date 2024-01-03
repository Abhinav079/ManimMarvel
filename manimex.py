from manim import *

class ChainRuleVisualization(Scene):
    def construct(self):
        # Number lines
        line_x = NumberLine(
            x_range=[0, 3, 1],
            length=6,
            color=WHITE,
            include_numbers=True,
            label_direction=DOWN,
        )

        line_x2 = NumberLine(
            x_range=[0, 9, 1],
            length=6,
            color=WHITE,
            include_numbers=True,
            label_direction=DOWN,
        )

        # Position number lines
        line_x.to_edge(UP, buff=1)
        line_x2.to_edge(DOWN, buff=1)

        # Labels for the number lines
        label_x = MathTex("x").set_color(BLUE).next_to(line_x, LEFT)
        label_x2 = MathTex("x^2").set_color(BLUE).next_to(line_x2, LEFT)

        # Create the differentials on the number lines
        dx_label = MathTex("dx").set_color(YELLOW).next_to(line_x.get_right(), RIGHT)
        dx2_label = MathTex("d(x^2)").set_color(YELLOW).next_to(line_x2.get_right(), RIGHT)

        # Create a tracker for x
        x_tracker = ValueTracker(1.5)
        x_value = x_tracker.get_value()

        # Triangle pointers for x and x^2
        triangle_x = Triangle().set_height(0.2).next_to(line_x.n2p(x_value), UP, buff=0.1)
        triangle_x2 = Triangle().set_height(0.2).next_to(line_x2.n2p(x_value**2), UP, buff=0.1)

        arc_1 = CurvedArrow(line_x.n2p(x_value), line_x2.n2p(x_value**2), color=GREEN)
        arc_2 = CurvedArrow(line_x2.n2p(x_value**2), line_x.n2p(np.sin(x_value**2)), color=BLUE)

        # Manually scale the tips if needed (this is usually not necessary)
        arc_1.tip.scale(0.5)
        arc_2.tip.scale(0.5)

        # Function labels
        label_sin = MathTex(r"\sin\left(x^2\right)").set_color(RED).next_to(arc_2, RIGHT)
        label_dsin = MathTex(r"d\left(\sin\left(x^2\right)\right)").set_color(RED).next_to(label_sin, DOWN)

        # Differential equation for sin(x^2)
        diff_eq = MathTex(r"\frac{d}{dx}\sin(x^2) = \cos(x^2) \cdot 2x").next_to(label_dsin, DOWN)
        
        # Adding everything to the scene
        self.add(line_x, line_x2, label_x, label_x2, dx_label, dx2_label, triangle_x, triangle_x2)
        self.play(GrowArrow(arc_1), GrowArrow(arc_2))
        self.play(Write(label_sin), Write(label_dsin), Write(diff_eq))

        self.wait()
