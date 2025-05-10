# Basic Tutorial for GUI Framework

This tutorial will guide you through the basics of using the GUI framework to create a simple window, add shapes, and interact with them.

---

## 1. **Setup and Requirements**

### Install Dependencies

Before getting started, ensure you have the required dependency: `pygame`. You can install it using pip:

pip install pygame

2. Creating a Window

To start with, we need to create a window for our application.
Example:

from window import Window

# Create a window with a title bar and size of 800x600 pixels
window = Window(title_bar=True, size=(800, 600))

# Start the event loop to display the window
window.loop()

Explanation:

    Window(title_bar=True, size=(800, 600)): Creates a new window with the specified size. The title_bar=True argument ensures that the window has a title bar.

    window.loop(): Starts the event loop where all the events, rendering, and shape updates are handled.

3. Adding Shapes to the Window

You can add various shapes to the window. For example, adding a rectangle and a circle.
Example:

from shapes.rectangle import Rectangle
from shapes.circle import Circle

# Create a rectangle and a circle
rect = Rectangle(master=window)
circle = Circle(master=window)

# Add them to the window's shapes list
window.shapes.append(rect)
window.shapes.append(circle)

Explanation:

    Rectangle(master=window): Creates a rectangle object.

    Circle(master=window): Creates a circle object.

    window.shapes.append(): Adds the created shapes to the list of shapes to be rendered by the window.

4. Customizing Shapes

You can modify properties like size, color, position, and opacity for the shapes.
Example:

# Set the size and color of the rectangle
rect.size = (200, 100)
rect.color = (255, 0, 0)  # Red color

# Set the position of the circle
circle.position = (100, 100)

# Set the opacity of the rectangle
rect.opacity = 180  # 0 is fully transparent, 255 is fully opaque

Explanation:

    rect.size = (200, 100): Changes the size of the rectangle.

    rect.color = (255, 0, 0): Sets the color of the rectangle to red.

    circle.position = (100, 100): Changes the position of the circle on the window.

    rect.opacity = 180: Sets the opacity of the rectangle, where 255 is fully opaque and 0 is fully transparent.

5. Handling Events

You can handle mouse clicks, keyboard presses, and other events by using the event_catcher method.
Example:

def on_click(event):
    if event.type == pg.MOUSEBUTTONDOWN:
        print("Mouse clicked!")

# Add the event handler to the rectangle
rect.event_catchers.append(on_click)

Explanation:

    on_click(event): Defines a function to handle mouse clicks. It checks if the event is a mouse button down event and prints a message when clicked.

    rect.event_catchers.append(on_click): Adds the on_click event handler to the rectangle.

6. Rendering the Window

Finally, the window will continuously update and render the shapes with the window.loop() method.
Example:

# Start the window loop to display everything
window.loop()

Explanation:

    window.loop(): This keeps the window open and continuously renders all shapes and handles events.

7. Further Customizations
Additional Shape Customizations:

    Rotation: Rotate any shape using the angle property.

    Outline: Add outlines to shapes with the outline_width and outline_color properties.

    Opacity: Control the opacity of shapes by adjusting the opacity property (0 for fully transparent, 255 for fully opaque).

Example:

# Set the angle of rotation for the rectangle
rect.angle = 45  # Rotates the rectangle by 45 degrees

# Set the outline width and color
rect.outline_width = 5
rect.outline_color = (0, 0, 0)  # Black outline

# Apply blur effect (if supported)
rect.blur = 5  # Apply a blur effect with intensity 5

Conclusion

This tutorial covered the basics of creating a window, adding shapes, customizing them, and handling events. The framework provides a lot of flexibility to build interactive GUI applications. Explore more by experimenting with different shapes and properties!
Contact

Ben Nowakowski
Email: ben.nowa@icloud.com


### Key Points:
- **Basic Setup**: Install dependencies, create a window, and start the loop.
- **Shapes**: How to create and add shapes like rectangles and circles.
- **Customization**: How to modify shape properties such as size, color, and opacity.
- **Events**: Handling events like mouse clicks with the `event_catcher` method.
- **Rendering**: How the window continuously updates with `window.loop()`.

This should be placed as `tutorial.md` in your project directory to provide a guide for new users on how to get started with the framework.


ChatGPT can make mistakes. Check important info