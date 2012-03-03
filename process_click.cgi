#! /usr/bin/env python

import cgi, cgitb, os, getpixel, logic

# Alter as necessary
def image_mask_files (imgname):
    return imgname[:-4] + "_active%d.ppm.gz"


print "Content-type: text/plain"
print

data = cgi.FieldStorage ()

src = data.getfirst ("src")
session = data.getfirst ("session")
x = int(data.getfirst ("x"))
y = int(data.getfirst ("y"))
other = data.getfirst ("other")

if other and other != "":
    print logic.process_special (src, other, session, x, y)
    exit ()

mask_file_base = image_mask_files (src)
i = 1
while os.path.exists (mask_file_base % i):
    mask = open (mask_file_base % i)
    rgb = getpixel.getpixel (mask, x, y)
    if rgb == [255, 255, 255]:
        print logic.process (src, mask_file_base % i, session, x, y)
        break
    i += 1
