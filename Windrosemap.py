#!/usr/bin/python

# The ChartDirector for Python module is assumed to be in "../lib"
import PIL.Image as Image
from PIL import Image, ImageDraw, ImageFont
import sys, os
sys.path.insert(0, os.path.join(os.path.abspath(sys.path[0]), "..", "lib"))

from pychartdir import *

# Data for the chart
data = [91, 713, 6296, 13175, 28572, 62963, 17523, 4219, 21351, 15553, 14975, 13249, 2687, 1832, 5360, 1950, 530, 302, 2693, 818]
# Angles for the Windrosemap
angles = [0, 18, 36, 54, 60,72,90,108,126,144,162,180,198,216,234,252,270,288,306,324,342]


# Create a PolarChart object of size 460 x 460 pixels, with a silver background and a 1 pixel 3D
# border
# c = PolarChart(460, 460, silverColor(), 0x000000, 1)
c = PolarChart(460, 470, 0xFFFFFF, 0x000000, 0)

# Add a title to the chart at the top left corner using 15pt Arial Bold Italic font. Use white text
# on deep blue background.
cityname='Bzijing'
c.addTitle(cityname, "Arial Bold Italic", 15, 0x000000).setBackground(
    0xffffff)

# Set plot area center at (230, 240) with radius 180 pixels and white background
c.setPlotArea(230, 240, 180, 0xffffff)

# Set the grid style to circular grid
c.setGridStyle(0)

# Set angular axis as 0 - 360, with a spoke every 30 units
c.angularAxis().setLinearScale(0, 360, 90)

# Add sectors to the chart as sector zones
for i in range(0, len(data)) :
    c.angularAxis().addZone(angles[i], angles[i] + 18, 0, data[i], 0x0066CC, 0x000000)

# Add an Transparent invisible layer to ensure the axis is auto-scaled using the data
c.addLineLayer(data, Transparent)

# Output the chart
c.makeChart("rose.png")