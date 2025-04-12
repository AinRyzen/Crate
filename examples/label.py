import crate as c

# 🪟 Create a window object
win = c.Win()

# 🖋️ Create and configure a Label
label = c.Label(master=win)             # Master could be the window or another shape

# 🖌️ Label Appearance & Settings
label.position = (50, 50)               # X, Y position of the label on the screen
label.size = (200, 50)                  # Width, height of the label (may not be directly used)
label.text = "Hello Crate!"             # Text displayed on the label
label.font_size = 48                    # Font size of the label text
label.font_color = "#ffffff"            # Font color (HEX or RGB)
label.color = None                      # Background color (None for no background)
label.font_file_path = "path/to/font.ttf"  # Path to the font file
label.opacity = 255                     # Transparency level (0 = invisible, 255 = fully visible)
label.angel = 0                         # Rotation angle of the label (degrees)
label.blur = 0                          # Blur level to apply (0 = no blur)
label.show = True                       # Toggle visibility of the label

# ⚙️ Label Behavior & Events
label.event_catchers = []               # List of functions to handle input events for the label

# 🔁 Main loop and label update
win.ticks.append("label.tick")           # Add the label update function to be called every frame
win.event_catchers.append("label.event_catcher")  # Add event catcher to handle input events

# 🚀 Start the main loop
win.loop()  # Start the window's main loop to render and update the label
