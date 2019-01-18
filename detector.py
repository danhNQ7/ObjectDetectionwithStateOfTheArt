# Stupid python path shit.
# Instead just add darknet.py to somewhere in your python path
# OK actually that might not be a great idea, idk, work in progress
# Use at your own risk. or don't, i don't care

import sys, os
#sys.path.append(os.path.join(os.getcwd(),'python/'))

import darknet as dn
import pdb
from PIL import Image
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
labels ={'light':0,'car':1,'moto':2}
#dn.set_gpu(1)
net = dn.load_net(b"custom/yolov3.cfg", b"backup/yolov3_900.weights", 0)
meta = dn.load_meta(b"custom/obj.data")

PATH = 'dataset/test.txt'
with open(PATH,'r') as f:
    files = f.read().strip().split('\n')
for f in files:
    im = Image.open(f)
    fs = open('Predict/'+f[f.rfind('/')+1:-3]+'txt','w')
    width, height = im.size
    # source_img = Image.open(f)
    # draw = ImageDraw.Draw(source_img)
    # draw.text((20, 70), "something123", font=ImageFont.truetype("font_path123"))

    
    r = dn.detect(net, meta, bytes(f,encoding="ascii"))
    for result in r: 
        name = result[0].decode('ascii')
        xcenter = result[2][0]
        y_center = result[2][1]
        w = result[2][2]
        h = result[2][3]
        fs.write('{} {} {} {} {} {}\n'.format(labels[name],result[1],int(xcenter-w/2),int(y_center-h/2),int(xcenter+w/2),int(y_center+h/2)))
        # draw.rectangle(((int(xcenter-w/2),int(y_center-h/2)), (int(xcenter+w/2),int(y_center+h/2))), outline="black")
    # source_img.save('test.png', "png")
    fs.close()
    # print( r)

# And then down here you could detect a lot more images like

