import crate as c

# 🪟 Create a window object
win = c.Win()

# 🎨 Window appearance
win.color = "green"                     # Background color (supports HEX & RGB)
win.size = (500, 500)                   # Window size (width, height)
win.title = "Crate Window"              # Title displayed in the window's title bar
win.window_icon = None                  # Path to the window icon (None for default)
win.title_bar = True                    # Show/hide the title bar

# ⚙️ Window behavior
win.closeable = True                    # Allows closing the window via the title bar
win.allow_screensaver = True            # Allows screensaver while the window is open
win.fps = 120                           # Target frames per second (FPS)

# 🔁 Main loop functions
win.ticks.append("your_func")           # Add custom function to be called every frame
win.event_catchers.append("you_func")   # Add custom function to be called every time an event is caught

# 🚀 Start the main loop
win.loop()
