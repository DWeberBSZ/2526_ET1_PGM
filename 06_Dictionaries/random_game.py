"""
Winter Landscape Animation with Falling Snow
A beautiful serene animation featuring a winter landscape with trees and falling snow.
"""

import turtle
import random
import time

# Screen settings
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

class Snowflake:
    """Falling snowflake"""
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.shapesize(0.5, 0.5)
        
        # Random starting position
        x = random.randint(-SCREEN_WIDTH // 2, SCREEN_WIDTH // 2)
        y = random.randint(0, SCREEN_HEIGHT // 2)
        self.turtle.goto(x, y)
        
        # Random fall speed
        self.speed = random.uniform(0.5, 2)
    
    def fall(self):
        """Move snowflake down"""
        x = self.turtle.xcor()
        y = self.turtle.ycor() - self.speed
        
        # Slight wind effect
        wind = random.uniform(-0.3, 0.3)
        x += wind
        
        self.turtle.goto(x, y)
        
        # Reset if below screen
        if y < -SCREEN_HEIGHT // 2:
            self.turtle.goto(random.randint(-SCREEN_WIDTH // 2, SCREEN_WIDTH // 2), 
                            SCREEN_HEIGHT // 2)
    
    def hide(self):
        """Hide snowflake"""
        self.turtle.hideturtle()

class Tree:
    """Pine/evergreen tree"""
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.parts = []
    
    def draw(self):
        """Draw the tree"""
        # Draw trunk
        trunk = turtle.Turtle()
        trunk.penup()
        trunk.goto(self.x, self.y - self.size * 0.3)
        trunk.pendown()
        trunk.color("brown")
        trunk.width(self.size // 10)
        trunk.goto(self.x, self.y - self.size * 0.6)
        trunk.hideturtle()
        self.parts.append(trunk)
        
        # Draw evergreen layers
        colors = ["darkgreen", "green", "green"]
        layer_heights = [self.size * 0.4, self.size * 0.35, self.size * 0.3]
        layer_widths = [self.size * 0.6, self.size * 0.45, self.size * 0.3]
        
        for i, (height, width, color) in enumerate(zip(layer_heights, layer_widths, colors)):
            layer = turtle.Turtle()
            layer.penup()
            layer.goto(self.x, self.y - i * self.size * 0.25)
            layer.pendown()
            layer.color(color)
            layer.width(2)
            
            # Draw triangle (evergreen shape)
            for _ in range(3):
                layer.forward(width)
                layer.left(120)
            
            layer.hideturtle()
            self.parts.append(layer)
    
    def hide(self):
        """Hide tree"""
        for part in self.parts:
            part.hideturtle()

class Ground:
    """Snow-covered ground"""
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.goto(-SCREEN_WIDTH // 2, -SCREEN_HEIGHT // 2 + 50)
        self.turtle.pendown()
        self.turtle.color("white")
        self.turtle.width(3)
        self.turtle.goto(SCREEN_WIDTH // 2, -SCREEN_HEIGHT // 2 + 50)
        self.turtle.hideturtle()
    
    def hide(self):
        """Hide ground"""
        self.turtle.hideturtle()

class Animation:
    """Main animation controller"""
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.bgcolor("#E0F4FF")  # Light blue winter sky
        self.screen.title("Winter Landscape - Peaceful Falling Snow")
        self.screen.tracer(0)
        
        # Create elements
        self.snowflakes = [Snowflake() for _ in range(100)]
        self.ground = Ground()
        
        # Create trees of different sizes at different positions
        self.trees = [
            Tree(-350, -50, 80),
            Tree(-200, -80, 100),
            Tree(0, -30, 120),
            Tree(200, -70, 90),
            Tree(350, -40, 85),
            Tree(-450, 50, 60),
            Tree(400, 100, 70),
        ]
        
        # Draw all trees
        for tree in self.trees:
            tree.draw()
        
        # Title display
        self.title_display = turtle.Turtle()
        self.title_display.hideturtle()
        self.title_display.penup()
        self.title_display.color("darkblue")
        self.title_display.goto(0, SCREEN_HEIGHT // 2 - 40)
        self.title_display.write("Winter Landscape", align="center", 
                                 font=("Arial", 36, "bold"))
    
    def update(self):
        """Update animation"""
        # Update all snowflakes
        for snowflake in self.snowflakes:
            snowflake.fall()
        
        self.screen.update()
    
    def run(self):
        """Main animation loop"""
        try:
            while True:
                self.update()
                time.sleep(0.02)  # Control animation speed
        except KeyboardInterrupt:
            # Cleanup on exit
            for snowflake in self.snowflakes:
                snowflake.hide()
            self.ground.hide()
            for tree in self.trees:
                tree.hide()
            self.title_display.hideturtle()

# Run the animation
if __name__ == "__main__":
    animation = Animation()
    animation.run()
