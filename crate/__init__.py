#
# Coded by: Ben Nowakowski
# Contact: ben.nowa@icloud.com
#
# Commented by ChatGPT

# Imports
import pygame as pg

pg.init()  # Initialize Pygame

# Connections
from .window import Window  # Import the Window class for handling the main window
from .window import Window as Win  # Import Window again as an alias 'Win'

# ⤷ shapes
from .shapes.shape import Shape  # Import the base Shape class

# Import the Rectangle class and assign an alias 'Rect'
from .shapes.rectangle import Rectangle
from .shapes.rectangle import Rectangle as Rect

# Import the Circle class for drawing circles
from .shapes.circle import Circle

# Import the Label class for adding text labels
from .shapes.label import Label

# Import the Image class for displaying images
from .shapes.image import Image

# Import the Line class for drawing lines
from .shapes.line import Line
