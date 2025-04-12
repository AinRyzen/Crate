import crate as c

# 🪟 Create a window object
win = c.Win()

# ⚪ Create and configure a Circle
circle = c.Circle(master=win)           # Master could be the window or another shape

# 🖌️ Circle Appearance & Settings
circle.position = (0, 0)                # X, Y position of the circle on the screen
circle.color = "red"                    # RGB or Hex color of the circle
circle.event_catchers = []              # List of functions to handle input events
circle.size = 50                        # Diameter of the circle in pixels
circle.show = True                      # Toggle visibility of the circle
circle.opacity = 255                    # Transparency level (0 = invisible, 255 = fully visible)

# 🚀 Start the main loop
win.loop()