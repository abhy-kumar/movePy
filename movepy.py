import shutil 
import os

path =r'<your path here>'
k = os.listdir(path) 
for k in k : 
    name, ext = os.path.splitext(k) 

    ext = ext[1:] 
  
    if ext == '': 
        continue

    if os.path.exists(path+'/'+ext): 
       shutil.move(path+'/'+k, path+'/'+ext+'/'+k) 

    else: 
        os.makedirs(path+'/'+ext) 
        shutil.move(path+'/'+k, path+'/'+ext+'/'+k) 
