# (C) Copyright 1996-2016 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.


# importing Magics module
from Magics.macro import *


ref = "shading_only_over_land"
# Setting of the output file name
output = output(
    output_formats=["png"], output_name_first_page_number="off", output_name=ref
)

# Setting the coordinates of the geographical area
projection = mmap(
    subpage_map_projection="mollweide",
    subpage_y_position=3,
    subpage_y_length=20,
    page_frame="off",
    subpage_frame="off",
)


# Coastlines setting
coast = mcoast(
    map_coastline_sea_shade="on",
    map_coastline_sea_shade_colour="charcoal",
    map_grid_colour="RGB(0.4,0.4,0.4)",
    map_grid_frame="on",
    map_label="off",
)


# Import the z500 data
data = mgrib(grib_input_file_name="2m_temperature.grib",)


# Define the simple contouring for z500
contour = mcont(
    contour_automatic_setting="style_name",
    contour_style_name="sh_all_fM64t52i4",
    legend="on",
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


title = mtext(
    text_lines=["Shading only over land"], text_font_size=0.6, text_colour="charcoal"
)


# To the plot
plot(output, projection, data, contour, title, coast, legend)
