
import pandas as pd
import barcode

pincode = int(input("Enter the Address Pin Code Where you want to deliver the post:"))

from barcode.writer import ImageWriter
number = pincode
Mycode = barcode.get_barcode_class('code39')
code39 = Mycode(number, writer=ImageWriter())
code39.save('barcodes/example2_barcode')
