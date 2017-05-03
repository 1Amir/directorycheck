import os

os.walk("/home")
[x[0] for x in os.walk("/home")]
next(os.walk('.'))[1]
print x
