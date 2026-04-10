# (C) Copyright 1996-2016 ECMWF.
# 
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0. 
# In applying this licence, ECMWF does not waive the privileges and immunities 
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.


#importing Magics module
from Magics.macro import *


ref = 'chem-co'

#Setting of the output file name
output = output(output_formats = ['png'],
        output_name_first_page_number = "off",
        output_name = ref)


#Import the z500 data
data =  mgrib(grib_input_file_name  = "chem-co.grib")

contour = mcont()

title = mtext(
           text_lines = ["<magics_title/>"],
           text_justification = "left",
           text_font_size = 0.42,
           text_colour =  "charcoal")


#To the plot
plot(output, data, contour, title)














