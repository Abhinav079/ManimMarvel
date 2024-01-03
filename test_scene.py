from manim import *

class Basic3DScene(ThreeDScene):
    def construct(self):
        # Create a 3D cube
        cube = OpenGLCube()

        # Rotate the cube
        self.play(Rotate(cube, axis=OUT, radians=PI/2))

        # Display the cube
        self.add(cube)
        self.wait(2)
