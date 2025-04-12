import crate as c

# 🪟 Create a window object
win = c.Win()

# ➖ Create and configure a Line
line = c.Line(master=win)                 # Master could be the window or another shape

# 🖌️ Line Appearance & Settings
line.start_position = (100, 100)          # Starting position of the line (X, Y)
line.end_position = (200, 200)            # Ending position of the line (X, Y)
line.size = 5                             # Thickness of the line
line.color = (255, 0, 0)                  # RGB color of the line (e.g., red)
line.opacity = 255                        # Transparency level (0 = invisible, 255 = fully visible)
line.angel = 0                            # Rotation angle of the line (degrees)
line.show = True                          # Toggle visibility of the line

# ⚙️ Line Behavior & Events
line.event_catchers = []                  # List of functions to handle input events for the line

# 🔁 Main loop and line update
win.ticks.append("line.tick")             # Add the line update function to be called every frame
win.event_catchers.append("line.event_catcher")  # Add event catcher to handle input events

# 🚀 Start the main loop
win.loop()  # Start the window's main loop to render and update the line
