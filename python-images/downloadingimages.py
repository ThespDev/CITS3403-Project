import requests
import shutil
import os

os.chdir('C:\\Users\\Cameron Roth\\CITS3403\\CITS3403-Project\\python-images\\')

lst = []
lst2 = []

with open('landmarks.txt', 'r') as file:
    for line in file:
        lst.append(line.strip())

with open('links.txt', 'r') as linkfile:
    for line in linkfile:
        lst2.append(line.strip())

for i in range(len(lst)):
    url = lst2[i]
    print('wp-content' in url)
    if 'wp-content' in url:
        continue
    filename = '{0}.jpg'.format(lst[i])
    print('saving picture...')
    res = requests.get(url, stream = True)
    print('picture requested!')
    downloaded = 0

    while downloaded == 0:

        if res.status_code == 200:
            with open(filename,'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ',filename)
            downloaded = 1
        else:
            print('Image Couldn\'t be retrieved, moving on')
            downloaded = 1