from manimlib import *

class MatrixTransformation(Scene):
    def construct(self):
        # Create axes and grid
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            width=10,
            height=10
        )
        grid = NumberPlane()
        self.add(axes, grid)

        # Basis vectors
        basis_vector_1 = Arrow(ORIGIN, [1, 0, 0], color=BLUE)
        basis_vector_2 = Arrow(ORIGIN, [0, 1, 0], color=YELLOW)
        self.add(basis_vector_1, basis_vector_2)

        # Transformation matrix
        matrix = np.array([[2, 1], [1, 2]])

        # Animate the transformation
        self.play(
            basis_vector_1.animate.apply_matrix(matrix),
            basis_vector_2.animate.apply_matrix(matrix),
            run_time=3
        )
        self.wait(2)

# Run the scene
if __name__ == "__main__":
    scene = MatrixTransformation()
    scene.render()
