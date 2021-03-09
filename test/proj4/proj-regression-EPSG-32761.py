from Magics.macro import *
import os

def plot_area(epsg):
	img = os.path.basename(__file__).split('.')[0]

	title = "Projection {} ".format(epsg)

	#Setting output
	png = output(
		output_formats                = ['png'],
		output_name                   = img,
		output_name_first_page_number = 'off')

	#Setting the geographical area
	area = mmap(
		subpage_map_projection         = epsg,
		
		subpage_map_area_definition    =  "full"
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


plot_area("EPSG:32761") 