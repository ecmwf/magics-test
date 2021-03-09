# (C) Copyright 1996-2016 ECMWF.
# 
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0. 
# In applying this licence, ECMWF does not waive the privileges and immunities 
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.


#importing Magics module
from Magics.macro import *


ref = 'gradient_shading'
#Setting of the output file name
output = output(output_formats = ['png'], 
		output_name_first_page_number = "off",
		output_name = ref)

#Setting the coordinates of the geographical area
projection = mmap(subpage_map_projection = 'robinson',
        subpage_map_vertical_longitude = -20,
        subpage_y_position= 3,
        subpage_y_length= 20,
        page_frame="off",
        subpage_frame="off",)


#Coastlines setting
coast = mcoast( map_grid="off", map_label="off", map_grid_frame = True,
                map_grid_frame_thickness = 5) 


#Import the z500 data 
data =  mgrib(grib_input_file_name  = "era5_t2_jan.grib",)


#Define the simple contouring for z500
contour = mcont(
        legend="on",
        contour="off",
        contour_level_selection_type="level_list",
        contour_level_list=[-45., -20, 0, 20, 45],
        contour_label="off",
        contour_shade="on",
        contour_shade_colour_method="gradients",
        contour_shade_method="area_fill",
        contour_gradients_colour_list=[
            "RGB(0.1532,0.1187,0.5323)",
            "RGB(0.5067,0.7512,0.8188)",
            "RGB(0.9312,0.9313,0.9275)",
            "RGB(0.9523,0.7811,0.3104)",
            "RGB(0.594,0.104,0.104)",
        ],
        contour_gradients_step_list=[20],
    )


legend = mlegend(
        legend_display_type = "continuous",
        legend_box_mode="positional",
        legend_text_font_size=0.4,
        legend_box_y_position=1,
        legend_box_y_length=1.5,
        legend_entry_border="off",
        legend_label_frequency=10,
    )


title = mtext( 
           text_lines = ["ERA5 T2 Monthly Mean 2020 January 0UTC"], 
           text_font_size=0.6,
           text_colour =  "charcoal")
	


#To the plot
plot(output, projection,  data, contour, title, coast, legend)















