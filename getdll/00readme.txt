I am not good at using LWP or http get method.
So my work flow to fetch objects from an HTML file:

1. parse the html file to retrieve all URLs I want
2. dump those URLs to a text file for example:
	http://foo.com/aFx.jpg
	http://foo.com/mVx.jpg
	...
3. use ''wget -i url.txt'' to retrieve those objects


Mar 29 2009, obsoleted script bt ../web/get_ppm_dll.pl
