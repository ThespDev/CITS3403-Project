from PIL import Image
import os
c=[0,0,0] # will store average r,g,b values for each pf_block i.e pf*pf

def avg(l,k):
    return l//(k*k)

def iterateThroughKbox(k,Xoffset,Yoffset,pix):
    for i in range (k):
        for j in range (k):
            c[0]+=pix[i+Xoffset,j+Yoffset][0]
            c[1]+=pix[i+Xoffset,j+Yoffset][1]
            c[2]+=pix[i+Xoffset,j+Yoffset][2]
    return (avg(c[0],k),avg(c[1],k),avg(c[2],k))


def assignAvg(k,Xoffset,Yoffset,pix,avg):
    for i in range (k):
        for j in range (k):
            pix[i+Xoffset,j+Yoffset]=tuple(avg)
            
            
def doStuff(k,i,j,pix):
    avg=iterateThroughKbox(k,i*k,j*k,pix)
    assignAvg(k,(i*k),j*k,pix,avg)
    c[0]=0
    c[1]=0
    c[2]=0


def pixel(img,pixel_factors): #@params img= string path to the image , pixel_factor= list of pixelation factors for 5 attempts
    
   
    path='./app/static/images/images/'
    img_path= path+img
    im = Image.open(img_path)
    pix = im.load()
    row=im.size[0]
    col= im.size[1]
    count=len(pixel_factors)+1
    for pf in pixel_factors:
        if pf!=0:
            block_row=row//pf # creating a block of area pf*pf to go through the image
            block_col=col//pf
            for i in range(block_row):
                for j in range(block_col):
                    doStuff(pf,i,j,pix)
        count-=1
        destination='./app/static/images/'+'tmp/'+str(count)+img[-4:]
        print(destination)
        im.save(destination)


