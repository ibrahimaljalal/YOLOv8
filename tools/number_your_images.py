#this script will copy all of the images from one folder and add them to another folder 
#the copied images will be numbered from the "counter" variable and increase by one
#you could optionally add a description after the number
#the only things you need to change in this script are the four variables between the multiple "#"
#if you did not change the "images_src_path" & "images_destination_path" variables, 
#then the images should be coped from the source folder to the destination folder

import re
import shutil
import os

#variables to change
######################################
images_src_path = "source" # images will be copied from this path
images_destination_path = "destination" # images will be copied to this path
counter = 1 #first number
additional_description ="_resource_1" #this will be added after the number to give more description. for example if additional_description = "_class_car" and the counter reached 51 then the result is 51_class_car.jpg
######################################

currentFilePath=os.path.dirname(os.path.realpath(__file__))
os.chdir(currentFilePath)

images_src_path += "/"
images_destination_path += "/"


for file_path in os.listdir(images_src_path):
    
    string = file_path

    pattern = ".*(?=\.(jpg|jpeg|JPEG|JPG|png|PNG|webp))"
    substitution = str(counter)+additional_description
    result = re.sub(pattern, substitution, string,count=1, flags=0)

    src = images_src_path+file_path
    dst = images_destination_path+result
    shutil.copyfile(src, dst)
    counter = counter + 1