import crate as c

# 🪟 Create a window object
win = c.Win()

# 🖼️ Create and configure an Image
image = c.Image(master=win)                 # Master could be the window or another shape

# 🖌️ Image Appearance & Settings
image.position = (100, 100)                # X, Y position of the image on the screen
image.size = (200, 200)                    # Width, height of the image
image.image_path = "path/to/image.png"     # Path to the image file
image.opacity = 255                        # Transparency level (0 = invisible, 255 = fully visible)
image.show = True                          # Toggle visibility of the image
image.blur = 0                             # Level of blur applied (0 = no blur)
image.angel = 0                            # Rotation angle of the image (degrees)

# ⚙️ Image Behavior & Events
image.event_catchers = []                  # List of functions to handle input events for the image

# 🔁 Main loop and image update
win.ticks.append("image.tick")             # Add the image update function to be called every frame
win.event_catchers.append("image.event_catcher")  # Add event catcher to handle user input

# 🚀 Start the main loop
win.loop()  # Start the window's main loop to render and update the image
