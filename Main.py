import os
root = "/home"
path = os.path.join(root, "directory")
for path, subdirs,files in os.walk(root):
    for name in files:
        print os.path.join(path, name)
