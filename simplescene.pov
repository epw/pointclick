#include "colors.inc"
#include "woods.inc"

#declare HEAD_HEIGHT = 2;

#declare ACTIVE_ID = 1;

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

#macro Active_Object (OBJ)
object {
	OBJ
#ifdef (Active)
#if (Active = ACTIVE_ID)
	texture { pigment { color White }
		  finish { ambient 2 }
	  }
#end
#end
}
#declare ACTIVE_ID = ACTIVE_ID + 1;
#end

Active_Object (
sphere { <0, 5, 2>, 1
	texture {
		pigment { color Red }
	}
})

Active_Object (
box { <-1, 5, 0>, <-2, 6, 1>
	texture {
		pigment { color Green }
	}
})
