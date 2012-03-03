#include "colors.inc"
#include "woods.inc"

#declare HEAD_HEIGHT = 2;

#declare ACTIVE_ID = 0;

#ifdef (Active)
#default {
	finish {
		ambient rgb<0, 0, 0>
	}
}
#end

camera {
	location <0, 0, HEAD_HEIGHT>
	look_at <0, 5, HEAD_HEIGHT>
	up <0, 0, 1>
	sky z
}

background { color rgb<0, 0, 0> }

#ifndef (Active)
light_source { <0, 0, 10> color rgb<.7, .7, .7> }
#end

plane { z, 0
	texture { P_WoodGrain1A
//		rotate 90*x
	}
}

#declare Interesting_Sphere =
sphere { <0, 5, 2>, 1
	texture {
		pigment { color Red }
	}
};

#macro Active_Object (OBJ)
#declare ACTIVE_ID = ACTIVE_ID + 1;
object {
	OBJ
#ifdef (Active)
#if (Active = ACTIVE_ID)
	texture { pigment { color White }
		  finish { ambient 1 }
	  }
#end
#end
}
#end

Active_Object (Interesting_Sphere)

Active_Object (
box { <-1, 5, 0>, <-2, 6, 1>
	texture {
		pigment { color Green }
	}
})

// AFTER ALL RENDERING DONE, EXTRA CODE HERE

#ifndef (Active)

#fopen ActiveCountFile "activecount.txt" write
#write (ActiveCountFile, ACTIVE_ID)
#fclose ActiveCountFile

#end
