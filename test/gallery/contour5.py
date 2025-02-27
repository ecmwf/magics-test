# (C) Copyright 1996-2016 ECMWF.
# 
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0. 
# In applying this licence, ECMWF does not waive the privileges and immunities 
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.


#importing Magics module
from Magics.macro import *


ref = 'contour5'
#Setting of the output file name
output = output(output_formats = ['png'], 
		output_name_first_page_number = "off",
		output_name = ref)

#Setting the coordinates of the geographical area
projection = mmap(
				subpage_x_length = 24., 
				subpage_upper_right_longitude = 50.00,
        		subpage_upper_right_latitude = 65.00,
		        subpage_lower_left_latitude = 25.00,
			    subpage_lower_left_longitude = -20.00,
			    subpage_map_projection = 'cylindrical')



#Coastlines setting
coast = mcoast( map_grid =  "on",
                map_grid_colour  =  "grey",
                map_grid_thickness  =  2,
				map_coastline_colour =  "RGB(0.4,0.4,0.4)",
				map_coastline_thickness = 3)


#Import the t850 data 
t850 =  mgrib(grib_input_file_name  = "t850.grb",
              grib_field_position =  1)



#Define a contour using a predefined contour level_list
contour = mcont( legend = "on",
				contour_level_selection_type = "level_list",
				contour_level_list=[-20., -10., -5., -2.5, -1, -0.5, 0., 0.5, 1, 2.5, 5, 10, 20, 50],
                contour_line_colour = "grey",
                contour_line_thickness =  2,
                contour_label =  "off",
				contour_highlight="off",
                contour_shade = "on",
                contour_shade_method = "area_fill",
				contour_shade_colour_method = "calculate",
				contour_shade_max_level_colour = "red",
				contour_shade_min_level_colour = "blue",
				contour_shade_colour_direction = "clockwise"
				)
                


title = mtext(
           text_lines = ["<font size='1'>Using Shading and positional legend ...</font>",
		   	"<font colour='evergreen'>contour_level_selection_type = level_list</font> ", 
			"    uses a user-defined list of contour levels.",
			"[-20., -10., -5., -2.5, -1, -0.5, 0., 0.5, 1, 2.5, 5, 10, 20, 50]"],
		   text_justification = "left",
		   text_font_size = 0.8,
           text_colour =  "charcoal")


legend = mlegend(legend='on', 
				legend_display_type='continuous',
				legend_border='off', 
				legend_title='on', 
				legend_title_text='My Title',
				legend_title_orientation='vertical',
				legend_text_font_size=0.5,
				legend_text_colour="navy",
				legend_box_mode ='positional',
				legend_box_x_position = 26.,
				legend_box_x_length=2.,
				legend_box_y_position=2.,
				legend_box_y_length=10.
				)

#To the plot
plot(output, projection, t850, contour, coast, legend,title)

#For documentation only
tofortran(ref, output, projection, t850, contour, coast, legend,title)
tomv4(ref, contour)
tohtml(ref, t850, contour)














