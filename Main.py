import os

os.walk("/home/amir")
[x[0] for x in os.walk("/home/amir")]
next(os.walk('.'))[1]
print x
