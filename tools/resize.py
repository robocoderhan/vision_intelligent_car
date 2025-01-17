# -*-coding:utf-8-*-

import os
from PIL import Image

def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.png')]

def image_dir_resize(imlist, width, height):
    for infile in imlist:
        Image.open(infile).resize((width, height)).save(infile)

if __name__ == '__main__':
    imlist = get_imlist("../samples/negative")
#    print imlist
    image_dir_resize(imlist, 45, 25)
