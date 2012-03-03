CFLAGS =

all:

simplescene: simplescene.pov
	povray $(CFLAGS) simplescene.ini
	$(foreach i,$(shell seq `cat activecount.txt`), \
		povray $(CFLAGS) simplescene.ini[Active] Declare=Active=$i \
			-Osimplescene_active$i.ppm; gzip -f simplescene_active$i.ppm; )
