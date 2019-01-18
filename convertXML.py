import xml.etree.ElementTree
import os
labels ={'light':0,'car':1,'moto':2}
PATH = 'dataset/Annotations'
PATHSAVE = 'groundtruth'
# files = os.listdir(PATH)
with open('dataset/test.txt','r') as f: 
    files = f.read().strip().split('\n')
for f in files:
    print(f[f.rfind('/')+1:-3]+'xml')
    # e = xml.etree.ElementTree.parse(os.path.join(PATH,f)).getroot()
    e = xml.etree.ElementTree.parse(os.path.join(PATH,f[f.rfind('/')+1:-3]+'xml')).getroot()
    with open(os.path.join(PATHSAVE,f[f.rfind('/')+1:-3]+'txt'),'w') as ff:
# print(e.findall('object'))
        width,height = int(e.find('imagesize/ncols').text) ,int(e.find('imagesize/nrows').text )
        for atype in e.findall('object'):
            if atype.find('deleted').text !='1':
                name =atype.find('name').text
                pointx =[int(a.text) for a in atype.findall('polygon/pt/x')]
                pointy =[int(a.text) for a in atype.findall('polygon/pt/y')]
                # print(pointx)
                xmin,xmax = min(pointx),max(pointx)
                ymin,ymax = min(pointy),max(pointy)
                #ff.write('{} {} {} {} {}\n'.format(labels[name],(xmin+xmax)/(2.0*width),(ymin+ymax)/(2.0*height),(xmax - xmin)*1.0/width,(ymax-ymin)*1.0/height))
                ff.write('{} {} {} {} {}\n'.format(labels[name],xmin,ymin,xmax,ymax))
