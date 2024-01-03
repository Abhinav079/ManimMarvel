from manim import *

class MatrixTransformation(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors=True
        )

    def construct(self):
        # Transformation matrix
        matrix = [[0, -1], [1, 0]]

        # Create smaller matrix and text to fit on screen
        matrix_mob = Matrix(matrix, element_to_mobject_config={"font_size": 24}).to_edge(UL)
        

        # Add matrix and text as separate layer
        self.add_foreground_mobjects( matrix_mob)
        
        # Apply the transformation
        self.apply_matrix(matrix)
        self.wait(2)

        # You can add more explanatory texts or visual elements as needed

# Set background color to dark (similar to 3Blue1Brown style)
config.background_color = "#1e1e1e"
