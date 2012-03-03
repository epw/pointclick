#! /usr/bin/env python

import cgi, cgitb, os, getpixel

err = open ("args.txt", "w")

# Alter as necessary
def image_mask_files (imgname):
    return imgname[:-4] + "_active%d.ppm.gz"


print "Content-type: text/plain"
print

data = cgi.FieldStorage ()

src = data.getfirst ("src")
x = int(data.getfirst ("x"))
y = int(data.getfirst ("y"))

err.write ("src: " + src + "\n")

mask_file_base = image_mask_files (src)
i = 1
while os.path.exists (mask_file_base % i):
    err.write (mask_file_base % i + "\n")
    mask = open (mask_file_base % i)
    rgb = getpixel.getpixel (mask, x, y)
    err.write (str(rgb) + "\n")
    if rgb == [255, 255, 255]:
        err.write ("Output: " + (mask_file_base % i) + "\n")
        print (mask_file_base % i)
        break
    i += 1

err.close ()
