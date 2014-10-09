#!/usr/bin/env python

# refer to:
# http://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-2/

print """Content-type: text/html

<form method="post" action="test_form.py">
<textarea name="comments" cols="40" rows="5">
Enter comments here...
</textarea>
<br/>
<input type="submit" value="Submit">
</form>"""

