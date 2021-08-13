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
ref = 'wind5'

#Setting of the output file name
output = output(output_formats= ['png'],
                output_name_first_page_number= 'off',
                output_name= ref,
                page_id_line="off")

#Setting the coordinates of the geographical area
area = mmap(subpage_upper_right_longitude= 18.0,
                 subpage_upper_right_latitude= 45.,
                 subpage_lower_left_longitude= 16.,
                 subpage_map_projection= 'cylindrical',
                 subpage_lower_left_latitude= 43.5 )


#Background Coastlines 
background = mcoast( map_coastline_sea_shade_colour= 'white',
                     map_coastline_land_shade_colour= 'grey',
                     map_grid= 'off',
                     map_coastline_land_shade= 'on',
                     map_coastline_sea_shade= 'on',
                     map_label= 'off',
                     map_coastline_colour= 'tan')

#Foreground Coastlines
foreground = mcoast(  map_grid= 'on',
		      map_grid_colour = 'tan',
		      map_label= 'off',
		      map_coastline_colour= 'tan',
		      map_coastline_land_shade= 'off',
                      map_coastline_sea_shade= 'off')

#Import the  wind  at 200hPa uv200 
uv =  mgrib( grib_input_file_name = './inca.grb',
                grib_wind_position_1 =  4,
                grib_wind_position_2 =  5
            )

arrows = mwind(
                legend= 'on',
                wind_field_type = 'arrows',
		wind_arrow_unit_velocity = 10.0,
		wind_arrow_min_speed = 0.0,  
        wind_arrow_calm_below = 0.1,              
		wind_advanced_method = 'on',
		wind_advanced_colour_selection_type = 'interval',
		wind_advanced_colour_level_interval = 0.5,
		wind_advanced_colour_reference_level = 0,
		wind_advanced_colour_max_value = 10.0,
		wind_advanced_colour_min_value = 0.0,
		wind_advanced_colour_table_colour_method = 'calculate',
		wind_advanced_colour_direction = 'anti_clockwise',
		wind_advanced_colour_min_level_colour = 'turquoise',
        wind_thinning_factor =  10,
        wind_thinning_method =  "automatic",
		wind_advanced_colour_max_level_colour = 'purple_red',)

title = mtext( text_lines = ["<font size='1'>Wind arrow colour is a function of speed</font>",
                            "<font size='1'>GRIB internal representation described with a ProjString</font>"],
	       text_justification = 'left',
	       text_font_size = 0.5,
	       text_colour = 'charcoal')

#add a legend
legend = mlegend(legend= 'on',
           legend_text_colour= 'charcoal',
           legend_box_mode= 'positional',
           legend_box_x_position= 23.5,
           legend_box_y_position= 4.,
           legend_box_x_length= 2.,
           legend_box_y_length= 12.,
           legend_border= 'off',
           legend_border_colour= 'charcoal',
           legend_box_blanking= 'on',
           legend_display_type= 'continuous',
           legend_title = 'on',
	   legend_title_text= 'Wind speed at 200 hPa',
	   legend_text_font_size = '0.5')

#To the plot
plot(output, area, background,uv, arrows,foreground, title, legend)
