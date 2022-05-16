from selenium import webdriver
import time
from selenium.webdriver.common.by import By

import os

"""
Quick code to collect links to images from the internet.
Code uses microsoft edge to open up DuckDuckGo, find the first image response for a certain prompt and save the link.
downloadingimages.py attempts to download the image - will not work in some instances
(most common marker of failed images is the presence of wp-content in the URL)
"""

#Set this to where you want the text file of image links to be saved
os.chdir('C:\\Users\\Cameron Roth\\CITS3403\\CITS3403-Project\\python-images\\')

lst = []

with open('landmarks.txt', 'r') as file:
    for line in file:
        lst.append(line.strip())

file = open('links.txt', 'w')

print(lst)

start = 'https://duckduckgo.com/?q=images&t=h_&iax=images&ia=images'

#Set this to the directory the driver is in (I'll include this in the branch)
driver = webdriver.Edge(executable_path=r"C:\\Users\\Cameron Roth\\GCRL\\WebDrivers\\msedgedriver.exe")

driver.get(start)

for location in lst:
    driver.get('https://duckduckgo.com/?t=ffab&q={0}&atb=v211-1&iax=images&ia=images'.format(location.replace(" ", '+')))
    print("going to images...")
    time.sleep(6)
    print('finding first image...')
    pic = driver.find_element(By.XPATH, "//img[@class='tile--img__img  js-lazyload']")
    pic.click()
    time.sleep(5)
    print('finding button....')
    url = driver.find_element(By.XPATH, "//a[@class='c-detail__btn c-detail__btn--bottom btn js-image-detail-link']").get_attribute('href')
    'c-detail__btn c-detail__btn--bottom btn js-image-detail-link'
    file.write(url + '\n')
    time.sleep(3)
    
file.close()
driver.__exit__