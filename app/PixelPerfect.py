# from winreg import QueryReflectionKey
from email.mime import image
from unicodedata import name
from flask import app
from pathlib import Path
from PIL import Image
from config import Config
from datetime import datetime,timedelta
import shutil
import os
from flask_sqlalchemy import SQLAlchemy
# from app import models
from .models import User,Player_history,Images
UPLOAD_FOLDER=Config.UPLOAD_FOLDER


c=[0,0,0] # will store average r,g,b values for each pf_block i.e pf*pf

def remove_directory():  # will remove puzzle with the day before yesteday's date

    remove_date=datetime.strftime(datetime.now() - timedelta(2), '%m-%d-%Y')
    path=UPLOAD_FOLDER+ remove_date
    try:
        shutil.rmtree(path)
    except OSError:
        print ("del of the directory %s failed" % path)
        return False
    else:
        print ("del of the directory succeeded %s " % path)
        return True

def create_new_directory():
    today=datetime.strftime(datetime.now(), '%m-%d-%Y')
    path=os.getcwd()+'/app/static/images/'+ str(today)

    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
        return False
    else:
        print ("Successfully created the directory %s " % path)
        return True
    pass
def create_new_puzzle():

    today=datetime.strftime(datetime.now() - timedelta(0), '%m-%d-%Y')
    print(today)
    remove_directory()
    create_new_directory()
    image= Images.query.filter_by(date=today).first()
    populate_directories([image])
    print(image.name)


def get_dates():
    dates=[]

    yesterday=datetime.strftime(datetime.now() - timedelta(1), '%m-%d-%Y') 
    dates.append(yesterday)
    
    today=datetime.strftime(datetime.now(), '%m-%d-%Y')
    dates.append(today)
    tomorrow=datetime.strftime(datetime.now() + timedelta(1), '%m-%d-%Y') 
    dates.append(tomorrow)

    return dates

def create_directories():
    dates=get_dates()
    for date in dates:
        path=UPLOAD_FOLDER+ date
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)
    
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
            
            
def pixelate(k,i,j,pix):
    avg=iterateThroughKbox(k,i*k,j*k,pix)
    assignAvg(k,(i*k),j*k,pix,avg)
    c[0]=0
    c[1]=0
    c[2]=0

def get_images(dates):
    images=[]
    print(dates)
    for date in dates:
        print(date)
        image= Images.query.filter_by(date=date).first()
        
        print(image)
        images.append(image)

    return images




def populate_directories(images):
    if len(images)==1: 
        pixelelate(images)
    else:
        print('im here')
        pixelelate(images)

def initialiseGame():
    dates=get_dates()
    create_directories() # create 3 directories with yesterday,today's, and tomorrow's dates in that order
    print("immhere",dates)
    images=get_images(dates) #return a list of image obje in the format (path to image,date associated with image,pixelFactor)
    populate_directories(images) # populate directories with pixelated images
   


def pixelelate(images): #@params list of tupples [(image name(string),date(string),pixel factor(lst of ints))]
    print('in pixel')
    for image in images:
        image_name=image.name
        image_date=image.date
        pixel_factor=image.pf.split('/')
        pixel_factor=[int(pf) for pf in pixel_factor ]
        print(pixel_factor)
        img_path= UPLOAD_FOLDER+'images/'+image_name

        im = Image.open(img_path)
        pix = im.load()

        row=im.size[0]
        col= im.size[1]
        count=len(pixel_factor)+1
        for pf in pixel_factor:
            if pf!=0:
                block_row=row//pf # creating a block of area pf*pf to go through the image
                block_col=col//pf
                for i in range(block_row):
                    for j in range(block_col):
                        pixelate(pf,i,j,pix)
            count-=1
            print(image_date)
            destination=UPLOAD_FOLDER+image_date+'/'+str(count)+image_name[-4:]
            print(destination)
            im.save(destination)


#create_directories()
#remove_directory()
# initialiseGame()
# create_new_puzzle()