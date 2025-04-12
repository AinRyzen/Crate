import crate as c

# 🪟 Create a window object
win = c.Win()

# ▪️ Create and configure a Rectangle
rectangle = c.Rectangle(master=win)        # Master could be the window or another shape

# 🖌️ Rectangle Appearance & Settings
rectangle.position = (50, 50)              # X, Y position of the rectangle on the screen
rectangle.size = (200, 100)                # Width, height of the rectangle
rectangle.roundness = 10                   # Border radius for rounded corners
rectangle.color = (255, 0, 0)              # RGB color of the rectangle (e.g., red)
rectangle.opacity = 255                    # Transparency level (0 = invisible, 255 = fully visible)
rectangle.angel = 0                        # Rotation angle of the rectangle (degrees)
rectangle.show = True                      # Toggle visibility of the rectangle

# ⚙️ Rectangle Behavior & Events
rectangle.event_catchers = []              # List of functions to handle input events for the rectangle

# 🔁 Main loop and rectangle update
win.ticks.append("rectangle.tick")          # Add the rectangle update function to be called every frame
win.event_catchers.append("rectangle.event_catcher")  # Add event catcher to handle input events

# 🚀 Start the main loop
win.loop()  # Start the window's main loop to render and update the rectangle
