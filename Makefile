CFLAGS =

all:

simplescene: simplescene.pov
	povray $(CFLAGS) simplescene.ini
	povray $(CFLAGS) simplescene.ini Declare=Active=1 -Osimplescene_active1.png
