from manimlib import *
import numpy as np

class PiDayFourier(Scene):
    def construct(self):
        # Add title
        # Pi symbol (built-in version, works without SVG file)
        pi_symbol = Tex("\\pi").scale(15)
        pi_symbol.set_color(BLUE)
        pi_symbol.move_to(ORIGIN)
        
        # Extract points from the symbol
        points = pi_symbol.get_all_points()
        complex_points = np.array([complex(p[0], p[1]) for p in points])
        
        # Calculate Fourier coefficients
        n_vectors = 100
        coeffs = []
        for k in range(-n_vectors//2, n_vectors//2 + 1):
            c_k = np.sum(complex_points * np.exp(-2j * np.pi * k * np.arange(len(complex_points)) / len(complex_points))) / len(complex_points)
            coeffs.append((k, c_k))
        
        # Sort by magnitude and take top coefficients
        coeffs = sorted(coeffs, key=lambda c: abs(c[1]), reverse=True)
        coeffs = coeffs[:50]  # Use most significant coefficients
        
        # Create path for drawing
        drawn_path = VMobject()#
        drawn_path.set_points_as_corners([ORIGIN, ORIGIN])
        drawn_path.set_stroke(YELLOW, width=3)
        
        # Create epicycle groups
        circles = VGroup()
        vectors = VGroup()
        dots = VGroup()
        
        # Store path points
        self.path_points = [ORIGIN]
        
        # Create epicycles with visible styling
        center = ORIGIN
        
        for i, (freq, coef) in enumerate(coeffs):
            radius = abs(coef)
            # Ensure minimum visible size for small coefficients
            visible_radius = max(radius, 0.03)
            
            # Create circle with visible styling
            circle = Circle(radius=visible_radius)
            circle.set_stroke(BLUE_D, width=1, opacity=0.6)
            circle.move_to(center)
            
            # Create vector with visible styling
            angle = np.angle(coef)
            vector = Line(
                circle.get_center(),
                circle.get_center() + visible_radius * np.array([np.cos(angle), np.sin(angle), 0])
            )
            vector.set_stroke(RED, width=2)
            
            # Create dot at connection point
            dot = Dot(vector.get_end(), radius=0.02, color=WHITE)
            
            # Add to groups
            circles.add(circle)
            vectors.add(vector)
            dots.add(dot)
            
            # Update center for next epicycle
            center = vector.get_end()
        
        # Add all elements to scene
        self.add(circles, vectors, dots, drawn_path)
        
        # Define update function for animation
        def update_path(mob, dt):
            t = self.time * 0.2  # Control drawing speed
            
            center = ORIGIN
            for i, (freq, coef) in enumerate(coeffs):
                # Calculate new positions based on Fourier coefficients
                radius = abs(coef)
                phase = np.angle(coef)
                visible_vectors = min(50, int(10 + self.time * 2))  # Start with 10, add 
                
                # Position circle
                circles[i].move_to(center)
                
                # Calculate rotation based on frequency and time
                angle = phase + 2 * PI * freq * t
                new_end = center + radius * np.array([np.cos(angle), np.sin(angle), 0])
                
                # Update vector
                vectors[i].put_start_and_end_on(center, new_end)
                
                # Update dot
                dots[i].move_to(new_end)
                
                # Update center for next epicycle
                center = new_end
            
            # Add point to drawn path
            self.path_points.append(center)
            if len(self.path_points) > 1000:
                self.path_points = self.path_points[-1000:]
            
            # Update path with visible styling
            mob.set_points_as_corners(self.path_points)
            
            # Use a single color instead of gradient
            # Inside update_path
            mob.set_stroke(YELLOW, width=5)
        
        # Add updater to path
        drawn_path.add_updater(update_path)

        self.wait(1)
                # Add Pi Day message
        pi_day = Text("Happy Pi Day!", font_size=36)
        pi_day.to_edge(DOWN, buff=0.5)
        self.play(Write(pi_day), run_time = 3)
        
        
        # Run animation for suitable duration
        self.wait(15)  # Show for 15 seconds
