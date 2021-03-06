# (C) Copyright 1996-2016 ECMWF.
# 
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0. 
# In applying this licence, ECMWF does not waive the privileges and immunities 
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.

# importing Magics module

from Magics.macro import *

ref = 'rotated'

# Setting of the output file name

output = output(output_formats=['png'],
                output_name_first_page_number='off',
                output_name=ref)

# Setting the coordinates of the geographical area

projection = mmap(subpage_map_projection='cylindrical',
                  subpage_lower_left_latitude=40.,
                  subpage_lower_left_longitude=-10.,
                  subpage_upper_right_latitude=70.,
                  subpage_upper_right_longitude=20.)

# Coastlines setting

coast = mcoast(map_grid='on', map_grid_colour='tan',
               map_coastline_land_shade='on',
               map_coastline_land_shade_colour='cream',
               map_coastline_colour='tan')

# Import the z500 data

z = mgrib(grib_input_file_name='z.grb')
wind = mgrib(grib_input_file_name='wind.grb')

# Define the simple contouring for z500

contour = mcont()
    
arrows = mwind(wind_thinning_factor = 3.00 )

title = \
    mtext(text_lines=["<font size='1'>Rotated grids</font>"], 
          text_justification='left', 
          text_font_size=0.8,
          text_colour='charcoal')

# To the plot

plot(
    output,
    projection,
    coast,
    z,
    contour,
    wind, arrows,
    title,
    )

