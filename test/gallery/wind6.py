# (C) Copyright 1996-2016 ECMWF.
# 
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0. 
# In applying this licence, ECMWF does not waive the privileges and immunities 
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.


#importing Magics module
from Magics.macro import *

#Example reference
ref = 'wind6'

#Setting of the output file name
output = output(output_formats= ['png'],
                output_name_first_page_number= 'off',
                output_name= ref)


#Setting the coordinates of the geographical area
europe = mmap( subpage_lower_left_latitude= 21.51,
               subpage_lower_left_longitude= -37.27,
               subpage_upper_right_latitude= 51.28,
               subpage_upper_right_longitude= 65.0,
               subpage_map_projection= "polar_stereographic")

#Background Coastlines 
foreground = mcoast({"map_coastline_colour": "black",
                     "map_coastline_land_shade": "off",
                     "map_coastline_sea_shade": "off",
                     "map_grid": "off",
                     "map_label": "off"})


#Import the  wind
uv700 =  mgrib( grib_input_file_name = './wind.grib',grib_id= 'uv700', grib_wind_style=True)

styles = wmsstyles(uv700)

print(styles)
               
uv700_wind = mwind(wind_automatic_setting = "ecmwf")

title = mtext( text_lines = ["<font size='1'>Automatic wind styling</font>"],
		text_mode= 'positional',
		text_box_x_position= 1.0,
		text_box_y_position= 17.5,
		text_box_x_length= 27.0,
		text_box_y_length= 2.3,
	       text_justification = 'centre',
	       text_font_size = 0.5,
	       text_colour = 'charcoal')



legend = mlegend(legend= 'on',
           legend_box_mode= 'positional',
           legend_box_x_position= 1.0,
           legend_box_y_position= 16.0,
           legend_box_x_length= 27.0,
           legend_box_y_length= 1.5,
           legend_text_colour= 'black',
           legend_border= 'off',
           legend_border_colour= 'black',
           legend_box_blanking= 'on',
           legend_display_type= 'continuous',
	   legend_text_font_size = 0.5)

#To the plot
plot(output,europe,uv700,uv700_wind,foreground,title, legend)

