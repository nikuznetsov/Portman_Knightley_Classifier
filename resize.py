from PIL import Image
import os, sys

path = ''
dirs = os.listdir( path )

def resize(dirs):
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((200,200), Image.ANTIALIAS)
            imResize.save(f + '.png', 'PNG', quality=90)

resize(dirs)