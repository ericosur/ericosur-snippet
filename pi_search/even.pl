#!/usr/bin/perl

while (<>)  {

	if ( m/^[^\d]/ )  {
		next;
	}
	else  {
		s/ //g;
		s/:\d+//;
		print;
	}
}
