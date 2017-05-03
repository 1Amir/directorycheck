import os

os.walk("/home/amir")
[x[0] for x in os.walk("/home/amir")]
while x > 0:
    next(os.walk('.'))[1]
    print x
