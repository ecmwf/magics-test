
from pyproj import Transformer
from pyproj import CRS

import random
from Magics.macro import *

import os
import jinja2


def plot_area(epsg, area, index):
	print (area)
	
	llx, lly, urx, ury = area
	img = os.path.basename(__file__).split('.')[0]

	title = "Projection {} : [{.2f}, {.2f}, {.2f}, {.2f}]".format(epsg, llx, lly, urx, ury)

	#Setting output
	png = output(
		output_formats                = ['png'],
		output_name                   = "{}-{}".format(img, index),
		output_name_first_page_number = 'off')

	#Setting the geographical area
	area = mmap(
		subpage_lower_left_latitude    = lly,
		subpage_lower_left_longitude   = llx,
		subpage_map_projection         = epsg,
		subpage_upper_right_latitude   = ury,
		subpage_upper_right_longitude  = urx,
		subpage_map_area_definition    =  "corners"
	)    

	#Setting the coastlines
	background = mcoast(
		map_coastline_land_shade        = 'on',
		map_coastline_resolution = "medium",
	    map_coastline_land_shade_colour = 'cream')


	#Picking the grib metadata
	title = mtext(
	    text_lines                     = [title],
	    text_justification             = 'left',
	    text_font_size                 = 0.6,
	    text_colour                    = 'charcoal')     

	#Plotting
	plot(png,area,background,title,)


def pcfull(epsg):
	if epsg  == "EPSG:3857": 
		return [ -20026376.39, -20048966.10, 20026376.3, 20048966.10] 
	if epsg  == "EPSG:4326": 
		return [ -180, -90, 180, 90 ]

	transformer = Transformer.from_crs("EPSG:4326", epsg,  always_xy=True)
	revert = Transformer.from_crs(epsg, "EPSG:4326", always_xy=True)
	ymin, x = transformer.transform(-0, 40)
	
	ymax, x = transformer.transform(180, 40)
	
	y, xmin = transformer.transform(-90, 40)
	
	y, xmax = transformer.transform( 90, 40)
	
	area =  [xmin, ymin, xmax, ymax]

	print (area)
	return area


def random_area(epsg):
	ymin, xmin, ymax, xmax = pcfull(epsg)

	width = 0
	while abs(width) < abs((xmax-xmin))*0.3:
		x1 = random.uniform(xmin, xmax*0.9)
		x2 = random.uniform(x1, xmax)
		width = (x2-x1)
		print (width, xmax-xmin)

	print ( "X1:{} < {} < {} [{}]".format(xmin, x1, xmax*0.9, xmax))
	print ( "X2:{} < {} < {} [{}]".format(xmin, x2, xmax*0.9, xmax))
	print ( "X:{} < {}".format(x1, x2) )

	
	height = width/2

	print ("Width={} height={}".format(width, height))

	y1 =  random.uniform(ymin, ymax-height)
	y2 = y1 + height

	print ( "Y1:{} < {} < {} [{}]".format(ymin, y1, ymax*0.9, ymax))
	print ( "Y2:{} < {} < {} [{}]".format(ymin, y2, ymax*0.9, ymax))
	print ( "Y:{} < {}".format(y1, y2) )


	revert = Transformer.from_crs(epsg, "EPSG:4326", always_xy=True)

	llx, lly = revert.transform(y1, x1)
	urx, ury = revert.transform(y2, x2)

	return [llx, lly, urx, ury]




index = 0
areas = {}
from jinja2 import Template


with open("proj.template",  "r") as source:
	template = jinja2.Template(source.read())
	
	for epsg in ["EPSG:32661", "EPSG:32761", "EPSG:3857", "EPSG:4326"]: 
		
		for i in range(1, 21):
			llx, lly, urx, ury = random_area(epsg)
			with open("proj-regression-EPSG-{}-{}.py".format(epsg.split(":")[1], i), "wt") as out:
				out.write(template.render(epsg = epsg, 
    						llx =llx, 
    						lly = lly, 
    						urx = urx, 
    						ury = ury 
                             ) )
             
	   

# epsg = "EPSG:32661"






# (C) Copyright 1996-2016 ECMWF.
# 
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0. 
# In applying this licence, ECMWF does not waive the privileges and immunities 
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.


#
