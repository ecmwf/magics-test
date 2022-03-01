# (C) Copyright 1996-2016 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.


# importing Magics module
from Magics.macro import *

ref = "obsjson"

# Setting of the output file name

output = output(
    output_formats=["png"], output_name_first_page_number="off", output_name=ref
)

# Setting the coordinates of the geographical area

projection = mmap(
    subpage_x_length=24.0,
    subpage_upper_right_longitude=50.00,
    subpage_upper_right_latitude=65.00,
    subpage_lower_left_latitude=25.00,
    subpage_lower_left_longitude=-20.0,
    subpage_map_projection="cylindrical",
)

# Coastlines setting

coast = mcoast(
    map_grid="on",
    map_grid_colour="grey",
    map_grid_thickness=2,
    map_coastline_colour="RGB(0.4,0.4,0.4)",
    map_coastline_thickness=3,
)


obs = mobs(
    obsjson_info_list=[
       {"type": "guan_plot", 
	"identifier": "toto", 
	"freq00": 4., 
	"gross00": 6., 
	"freq06": 6., 
	"gross06":0., 
	"freq12": 12., 
	"gross12": 12., 
	"freq18": 18., 
	"gross18": 18., 
	"longitude": 20, 
	"latitude": 50}
    ],
    obs_template_file_name="obs.template",
    obs_size=0.6,
    obs_ring_size=0.2,
    obs_distance_apart=0.0,
    obs_font_size=0.6,
)

title = mtext(
    text_lines=["Observation plotting ..."],
    text_justification="left",
    text_font_size=1.5,
    text_colour="charcoal",
)


# To the plot
plot(
    output, projection, obs, coast, title,
)
