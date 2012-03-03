#declare ACTIVE_ID = 0;

#ifdef (Active)
#default {
	finish {
		ambient rgb<0, 0, 0>
	}
}
#end

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

#macro Record_Active_Count ()
#ifndef (Active)

#fopen ActiveCountFile "activecount.txt" write
#write (ActiveCountFile, ACTIVE_ID)
#fclose ActiveCountFile

#end
#end
