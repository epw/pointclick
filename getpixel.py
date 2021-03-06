#! /usr/bin/env python

"""This program takes a single PPM file, gzip-compressed or not, and a
coordinate pair, and returns the (r, g, b) triplet at that point."""

import sys, gzip, cStringIO, os

def getpixel (imagefile, x, y):
    magicnumber = imagefile.read(2)
    if magicnumber == '\x1f\x8b': # GZIP magic number
        imagefile = gzip.open (imagefile.name)

    imgmap = cStringIO.StringIO(imagefile.read ())

    if magicnumber == '\x1f\x8b':
        imagefile.close ()

    pnmtype = ""
    width = 0
    height = 0
    depth = 0

    count = 0
    while count < 3:
        line = imgmap.readline ()
        if line[0] == "#":
            count -= 1
        else:
            if count == 0 and pnmtype == "":
                pnmtype = line.strip()
            elif count == 1 and width == 0:
                width, height = map (int, line.split ())
            elif count == 2 and depth == 0:
                depth = int(line)
        count += 1
    
    imgmap.seek ((y*width + x)*3, 1)

    return map (ord, imgmap.read(3))
    

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write ("Usage: %s [filename] x y\n" % sys.argv[0])
        sys.exit (1)
    elif len(sys.argv) == 3:
        result = getpixel (sys.stdin, int(sys.argv[1]), int(sys.argv[2]))
    else:
        if not os.path.exists (sys.argv[1]):
            sys.stderr.write ("File %s does not exist!\n" % sys.argv[1])
            sys.exit (1)
        with open (sys.argv[1]) as imagefile:
            result = getpixel (imagefile, int(sys.argv[2]), int(sys.argv[3]))

    print result
