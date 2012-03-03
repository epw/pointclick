CFLAGS =

all:

simplescene: simplescene.pov
	povray $(CFLAGS) simplescene.ini
	$(foreach i,$(shell seq `cat activecount.txt`), \
		povray $(CFLAGS) simplescene.ini Declare=Active=$i \
			-Osimplescene_active$i.png; done)

