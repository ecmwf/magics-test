# (C) Copyright 1996-2016 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.


# importing Magics module
from Magics.macro import *


ref = "xspole"
# Setting of the output file name
output = output(
    output_formats=["png"], output_name_first_page_number="off", output_name=ref
)

# Setting the cartesian view
projection = mmap(
    subpage_map_projection="cartesian",
    subpage_x_axis_type="regular",
    subpage_y_axis_type="regular",
    subpage_x_min=-65.0,
    subpage_x_max=-115,
    subpage_y_min=100.0,
    subpage_y_max=1,
)

# Vertical axis
vertical = maxis(
    axis_orientation="vertical",
    axis_grid="on",
    axis_type="regular",
    axis_grid_colour="grey",
    axis_grid_thickness=1,
    axis_grid_line_style="dot",
)

# Horizontal axis
horizontal = maxis(
    axis_orientation="horizontal",
    axis_grid="on",
    axis_tick_label_type="latitude",
    axis_grid_colour="grey",
    axis_grid_thickness=1,
    axis_grid_line_style="dot",
)


data = netcdf = mnetcdf(
    # netcdf_type = "matrix",
    netcdf_filename="xspole.nc",
    netcdf_y_variable="o3_lev",
    netcdf_x_variable="lat_for_plot",
    netcdf_field_automatic_scaling="off",
    netcdf_value_variable="o3",
)
contour = mcont(
    legend="on",
    contour_line_colour="charcoal",
    contour_highlight="off",
    contour_max_level=1.5e-5,
    contour_min_level=0,
    contour_shade="on",
    contour_shade_colour_method="palette",
    contour_shade_method="area_fill",
    contour_shade_palette_name="m_blue_green2_10",
)


title = mtext(
    text_lines=["Netcdf Xsection"],
    text_justification="left",
    text_font_size=1.0,
    text_colour="charcoal",
)


# To the plot
plot(output, projection, vertical, horizontal, data, contour, title)
