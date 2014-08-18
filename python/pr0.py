#!/usr/bin/python

movies = ["the holy grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

for item in movies:
    if isinstance(item, list):
        for name in item:
            print name
    else:
        print item
