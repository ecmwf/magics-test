# (C) Copyright 1996-2016 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http=//www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.

# importing Magics module
from Magics.macro import *


import numpy


ref = "geos0"
# Setting of the output file name

png = output(
    output_formats=["png"],
    output_name_first_page_number="off",
    output_name="%s" % (ref,),
)


# Setting the coordinates of the geographical area
projection = mmap(
    subpage_map_projection="geos",
    subpage_map_vertical_longitude=0.0,
    page_frame="off",
    subpage_frame="off",
)

# Import the z500 data
data = mgrib(grib_input_file_name="2m_temperature.grib",)


# Define the simple contouring for z500
contour = mcont(
    legend="on",
    contour="off",
    contour_shade="on",
    contour_shade_technique="cell_shading",
    contour_shade_max_level_colour="red",
    contour_shade_min_level_colour="blue",
    contour_shade_colour_direction="clockwise",
)

# Coastlines setting
coast = mcoast(
    map_grid="on",
    map_grid_colour="tan",
    map_coastline="on",
    map_coastline_colour="tan",
    map_coastline_style="solid",
)

# Title settings
title = mtext(
    text_lines=["<font size='1'> Shading on geos</font>"],
    text_justification="left",
    text_font_size=0.8,
    text_colour="charcoal",
)

legend = mlegend(
    legend_display_type="continuous",
    legend_box_mode="positional",
    legend_text_font_size=0.4,
    legend_box_y_position=1,
    legend_box_y_length=1.5,
    legend_entry_border="off",
    legend_label_frequency=10,
)

plot(png, projection, data, contour, legend, coast, title)
