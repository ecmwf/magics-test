
from  Magics import macro as magics

var = "impact"
data = "tamir.nc"
areas = {
    'Global': 'global',
    'Europe': 'europe',
}
        
png = magics.output(output_formats= ['png'],
                output_name_first_page_number= 'off',
                output_name= "tamir")

projection = magics.mmap(
    subpage_lower_left_latitude =  40.0,
    subpage_lower_left_longitude = -5.0,
    subpage_upper_right_latitude =  45.0,
    subpage_upper_right_longitude =  5.0,
    page_id_line                   = "off"

) 

background = magics.mcoast(
                     map_coastline_land_shade_colour= 'charcoal',
                     map_grid= 'off',
                     map_coastline_land_shade= 'on',
                     map_coastline_sea_shade= 'on',
                     map_coastline_sea_shade_colour= '#d6d6d6',
                     map_label= 'off',
                     map_coastline_colour= 'charcoal')


data = magics.mnetcdf(    
    netcdf_filename                  = data,
    netcdf_value_variable            = var,
    netcdf_dimension_setting         = "leadtime:13",
    netcdf_dimension_setting_method  = "index"
)

legend = magics.mlegend({
    "legend_display_type" : "continuous",
    "legend_text_colour" : "navy",
    "legend_entry_border" : "off",
})
symbol = magics.msymb(
    symbol_advanced_table_selection_type =  "list",
    symbol_advanced_table_level_list = [ 1.0,  2, 3, 4, 5],
    symbol_marker_index =  15,
    symbol_table_mode =  "advanced",
    symbol_advanced_table_height_method =  "list",
    symbol_advanced_table_height_list =  [0.5],
    symbol_advanced_table_colour_method =  "list",
    legend = True,
    symbol_advanced_table_colour_list =  ['RGB(255, 238, 160)' , 'RGB(253, 178, 76)' , 'RGB(189, 0, 38)' , 'RGB(106, 81, 164)'] )

magics.plot(png, projection, background, data, symbol, legend)


