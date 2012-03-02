#include "colors.inc"
#include "woods.inc"

#declare HEAD_HEIGHT = 2;

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

#ifdef (Active)
//global_settings { ambient_light rgb<0, 0, 0> }
#else
light_source { <0, 0, 10> color rgb<.7, .7, .7> }
#end

plane { z, 0
	texture { P_WoodGrain1A
//		rotate 90*x
	}
}

sphere { <0, 5, 2>, 1
#ifdef (Active)
#if (Active = 1)
	texture { pigment { color White }
		  finish { ambient 2 }
	  }
#end
#else
	texture {
		pigment { color Red }
	}
#end
}
