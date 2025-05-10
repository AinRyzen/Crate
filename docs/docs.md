# Project Documentation

## Overview

This project is a graphical user interface (GUI) framework built using Python and Pygame. The framework provides various graphical elements (shapes, labels, images, etc.) that can be rendered onto a window. The system allows easy creation and manipulation of graphical components in a window, offering flexibility to the user to design custom interfaces.

## Features

- **Window Management**: Create a window with customizable size, title, and more.
- **Shape Management**: Draw and manipulate different shapes like circles, rectangles, lines, and more.
- **Event Handling**: Handle mouse and keyboard events.
- **Transparency & Opacity**: Set transparency and opacity for shapes and window elements.
- **Positioning**: Dynamically adjust and update the position and size of elements.
- **Image Support**: Display images with optional outlines and opacity adjustments.



## Classes

### `Window`

This class is used to create and manage a window. It supports setting a title, background color, and other window properties. The `Window` class also has built-in methods for handling events like resizing, moving, and quitting the window.

#### Key Methods

- **`__init__(self, title_bar=True, size=(500, 500))`**: Initializes the window with the specified title bar and size.
- **`loop(self)`**: Starts the main event loop where window events and shape rendering are handled.
- **`reconfigure_window(self)`**: Moves the window when a manual position update is requested.
- **`centre_window(self)`**: Centers the window on the screen.

---

### `Shape` (Base Class)

The `Shape` class serves as a base class for all graphical elements. It defines methods for handling the rendering (`tick`) and event handling (`event_catcher`) for all shapes.

#### Key Methods

- **`tick(self, screen)`**: Renders the shape to the screen.
- **`event_catcher(self, event)`**: Handles events for the shape.

---

### `Rectangle`

The `Rectangle` class is used to create and render rectangles. It supports outlines, color, opacity, and corner roundness.

#### Key Methods

- **`tick(self, screen)`**: Renders the rectangle with or without an outline.
- **`initialize_variables(self)`**: Defines default properties like size, color, and outline width.

---

### `Circle`

The `Circle` class is used to create and render circles. It supports outlines, colors, opacity, and transparency.

#### Key Methods

- **`tick(self, screen)`**: Renders the circle, with or without an outline.
- **`initialize_variables(self)`**: Sets up the default values for size, color, and opacity.

---

### `Label`

The `Label` class is used to render text labels to the window. It supports font customization, color, opacity, and text display.

#### Key Methods

- **`tick(self, screen)`**: Renders the label to the screen.
- **`initialize_variables(self)`**: Sets up the label's properties like font size, text, and color.

---

### `Image`

The `Image` class is used to display images on the screen. It supports transparency, opacity, rotation, and blurring.

#### Key Methods

- **`tick(self, screen)`**: Renders the image to the screen, applying any transformations like rotation and blurring.
- **`initialize_variables(self)`**: Defines default properties such as image size, path, and opacity.

---

### `Line`

The `Line` class is used to render lines between two points on the screen. It supports thickness, color, opacity, and rotation.

#### Key Methods

- **`tick(self, screen)`**: Draws a line to the screen.
- **`initialize_variables(self)`**: Sets up default properties like size, color, and position.

---

## How to Use

1. **Create a Window**: Instantiate the `Window` class and call its `loop()` method to start the application.

   Example:
   ```python
   window = Window(title_bar=True, size=(800, 600))
   window.loop()

Add Shapes: You can create various shapes (Circle, Rectangle, Label, etc.) and add them to the window.

Example:

    circle = Circle(master=window)
    rectangle = Rectangle(master=window)

    Event Handling: Use the event_catcher method to handle events for specific shapes or the window itself.

    Customizing Shapes: You can customize shapes by modifying properties like color, opacity, size, etc.

Dependencies

    pygame: The Pygame library is used for window creation, event handling, and rendering graphics.

Install the dependencies using pip:

pip install pygame


### Documentation Breakdown:

- **Overview**: High-level summary of the project.
- **Features**: Key features of the framework, including window management and shape rendering.
- **Project Structure**: Shows the structure of the project files.
- **Classes**: Detailed description of each class (like `Window`, `Shape`, `Rectangle`, `Circle`, etc.) and their key methods.
- **How to Use**: Provides examples of how to use the framework to create windows and shapes, and handle events.
- **Dependencies**: Lists the external libraries required to run the project.
- **License and Contact**: Basic information about the license and how to contact the developer.

Feel free to modify this further or let me know if you want more details added!

