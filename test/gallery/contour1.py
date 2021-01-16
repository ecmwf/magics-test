# (C) Copyright 1996-2016 ECMWF.
# 
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0. 
# In applying this licence, ECMWF does not waive the privileges and immunities 
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.


#importing Magics module
from Magics.macro import *


ref = 'contour1'
#Setting of the output file name
output = output(output_formats = ['png'], 
		output_name_first_page_number = "off",
		output_name = ref)

#Setting the coordinates of the geographical area
projection = mmap(subpage_map_projection = 'geos',
        subpage_map_vertical_longitude = -20,
        subpage_x_position     = 20,
        subpage_y_position     = 3,
        subpage_x_length       = 86,
        subpage_y_length       = 86,)


#Coastlines setting
coast = mcoast( map_grid =  "on",
                map_grid_colour  =  "tan",
				map_coastline_land_shade  =  'on',
				map_coastline_land_shade_colour  =  'cream',
				map_coastline_colour =  "tan")


#Import the z500 data 
data =  mgrib(grib_input_file_name  = "sim_ir9.grib",)


#Define the simple contouring for z500
contour = mcont( contour_automatic_setting = "ecmwf",
        legend = "on" )


legend = mlegend(
        legend_text_font_size  = 0.25,
        legend_label_frequency = 3
        )


title = mtext(
           text_lines = ["<font size='1'>Simple Contouring...</font>",
		   			"<font colour='evergreen'>contour_level_selection_type = count</font> ", 
					"    calculate a reasonable  contour interval from the min and max of the displayed field"],
		   text_justification = "left",
		   text_font_size = 0.8,
           text_colour =  "charcoal")


#To the plot
plot(output, projection, coast, data, contour, title, legend)















