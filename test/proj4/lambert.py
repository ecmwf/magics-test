from Magics import macro

coast_params = {
    "map_coastline": "on",
    "map_coastline_land_shade": "off",
    "map_coastline_sea_shade": "off",
    "map_grid": "off",
    "map_label": "off",
}
map_params = {
    "subpage_map_projection": "EPSG:3857",
    "subpage_lower_left_latitude": -20820223.51242945,
    "subpage_lower_left_longitude": -20820223.51242945,
    "subpage_upper_right_latitude": 20820223.51242945,
    "subpage_upper_right_longitude": 20820223.51242945,
    "subpage_coordinates_system": "projection",
    "subpage_frame": "off",
    "page_x_length": 26.6,
    "page_y_length": 26.6,
    "super_page_x_length": 26.6,
    "super_page_y_length": 26.6,
    "subpage_x_length": 26.6,
    "subpage_y_length": 26.6,
    "subpage_x_position": 0.0,
    "subpage_y_position": 0.0,
    "output_width": 512,
    "page_frame": "off",
    "skinny_mode": "on",
    "page_id_line": "off",
}

args = [
    macro.output(
        output_formats=["png"],
        output_name_first_page_number="off",
        output_cairo_transparent_background="transparent",
        output_width=512,
        output_name="lambert",
    ),
    macro.mmap(**map_params),
    macro.mcoast(**coast_params),
]


macro.plot(*args)
