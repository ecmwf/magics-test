from Magics.macro import *

tiles = {
#"tile_1": [-20428865.927609347,-391357.58482010243, 391357.58482010243, 20428865.927609347],
"polar-tile": [-391357.58482010243, -20428865.927609347, 20428865.927609347, 391357.58482010243],
#"tile_3": [-20428865.927609347, -20428865.927609347, 391357.58482010243, 391357.58482010243]
}

coast = {'map_coastline': 'on', 
                'map_coastline_land_shade': 'on', 
                'map_coastline_sea_shade': 'on', 
                'map_grid': 'off', 
                'map_label': 'off'}

for k, v in tiles.items():
	png = {
	 "output_formats": ['png'],
	 "output_name_first_page_number": 'off',
	 "output_cairo_transparent_background": 'True',
	 "output_width": 1064,
	 "output_name": '{}'.format(k),
	}
 
	view = {
	 "subpage_map_projection": 'EPSG:32661',
	 "subpage_lower_left_latitude": v[0],
	 "subpage_lower_left_longitude": v[1],
	 "subpage_upper_right_latitude": v[2],
	 "subpage_upper_right_longitude": v[3],
	 "subpage_coordinates_system": 'projection',
	 "subpage_frame": 'off',
	 "page_x_length": 26.6,
	 "page_y_length": 26.6,
	 "super_page_x_length": 26.6,
	 "super_page_y_length": 26.6,
	 "subpage_x_length": 26.6,
	 "subpage_y_length": 26.6,
	 "subpage_x_position": 0.0,
	 "subpage_y_position": 0.0,
	 "output_width": 1064,
	 "page_frame": 'off',
	 "skinny_mode": 'on',
	 "page_id_line": 'off'}

	args = [output(**png), mmap(**view), mcoast(**coast)]

	# Plot the result
	plot(*args)
