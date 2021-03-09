from Magics.macro import *
import os


def plot_area(epsg, llx, lly, urx, ury):
    img = os.path.basename(__file__).split(".")[0]

    title = "Projection {} : [{:.2f}, {:.2f}, {:.2f}, {:.2f}]".format(
        epsg, llx, lly, urx, ury
    )

    # Setting output
    png = output(
        output_formats=["png"], output_name=img, output_name_first_page_number="off"
    )

    # Setting the geographical area
    area = mmap(
        subpage_lower_left_latitude=lly,
        subpage_lower_left_longitude=llx,
        subpage_map_projection=epsg,
        subpage_upper_right_latitude=ury,
        subpage_upper_right_longitude=urx,
        subpage_map_area_definition="corners",
    )

    # Setting the coastlines
    background = mcoast(
        map_coastline_land_shade="on",
        map_coastline_resolution="medium",
        map_coastline_land_shade_colour="cream",
    )

    # Picking the grib metadata
    title = mtext(
        text_lines=[title],
        text_justification="left",
        text_font_size=0.6,
        text_colour="charcoal",
    )

    # Plotting
    plot(
        png, area, background, title,
    )


plot_area(
    "EPSG:32661",
    -37.34747804175722,
    63.36483978934767,
    98.19766408377951,
    53.41815591456586,
)
