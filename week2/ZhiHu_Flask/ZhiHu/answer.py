
import os
basepath = os.path.dirname(__file__)
print(basepath)
path = os.path.join(basepath,'static/img/uploads/')
print(path)
for img in os.listdir(path):
    img_path = os.path.join(path,img)
    print(img_path)
    print(img)
    os.remove(img_path)