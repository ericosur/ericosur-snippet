'''
uuid demo
from: https://docs.python.org/2/library/uuid.html
'''
import uuid
import time

if __name__ == "__main__":
    for x in range(2):
        # uuid1: host id and current time
        print "uuid1: %s" % (uuid.uuid1())
        # uuid3: md5 hash namespace and a name
        print "uuid3: %s" % (uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org'))
        # uuid4: random uuid
        print "uuid4: %s" % (uuid.uuid4())
        # uuid5: sha1 hash namespace and a name
        print "uuid5: %s" % (uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org'))
        time.sleep(1)
        print '-' * 40
