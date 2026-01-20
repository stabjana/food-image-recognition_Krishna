from glob import *
import os
from PIL import Image


dir = '.'

os.system('mkdir %s/jpg' % dir)
webp_list = glob('%s/*.webp' % dir)

for webp in webp_list:
    im = Image.open(webp).convert('RGB')
    im.save('%s/jpg/%s.jpg' % (dir, webp[len(dir)+1:-5]), 'jpeg')
