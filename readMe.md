This code will read from your camera and detect objects by using an AI model from the "AI_models" folder.  

The main.py file is the starting point of your code.  

This code is written for the so far best and state of the art object detection AI model **"YOLO version 8"** (You Only Look Once).



# how to run the code:

it is highly recommended to use a virtual environment to avoid errors. Also, it is preferred to use the same python version.

python version: 3.9.13  
python link: https://www.python.org/downloads/release/python-3913/  
you do not need to download from the above link if you are going to use option 2.

## create a virtual environment and install all the dependencies:  

### option 1:
open your terminal and navigate to this working directory and write:
```
python -m venv virtual_environment  
.\virtual_environment\Scripts\activate  #Mac/linux: source virtual_environment/bin/activate
pip install -r requirements.txt  
python main.py 
```
### option 2 (if you have anaconda):
open your terminal and navigate to this working directory and write:
```
conda create -n virtual_environment python=3.9.13
activate virtual_environment
pip install -r requirements.txt  
python main.py 
```

# the primary files in this repository are:
1. main.py
2. requirements.txt
3. best.pt in the "AI_models" folder (you should add your traind file here. if not, you will use the example in this repository which is about construction site tools. the tools in the AI model: ['palm_tree', 'Goggles', 'Jacket', 'Gloves', 'Footwear']).  
    the rest of the files are made to help you train your own model. **if you delete them, you will not face any errors if you run main.py**


# other files/folders:
1. **train.ipynb** file (inside the "blob" folder):  
   this is the most important file for assisting you to train your own model. you should open it using google colab.
2. data_for_training_YOLOv8_models folder:  
    it contains the labeled & structured data for training YOLOv8. there is only one dataset (the "construction_site_objects" folder)
3. tools folder:  
   it will help you in labeling and naming your images. there are more detailed information in the files inside this folder.


# notes:
1. this code was tested in a windows 10 computer.
2. if you want to close the window after you ran the code, then pres the "Esc" key.
3. the best.pt file in the "AI_models" folder is the trained AI model on the "construction_site_objects" dataset in the "data_for_training_YOLOv8_models" folder. you can train your own model on your own dataset by following the steps in the train.ipynb file inside the "blob" folder. the train.ipynb file should be opened in a google colab. in practice you should give the best.pt file a more descriptive name & you could put multiple models in the "AI_models" folder. 
4. **if you use a CPU instead of a GPU, the speed will be about 30 time less!**
5. if you are plaining to use this code in your project then it is highly recommended to use "NVIDIA Jetson Nano" instead of the "Raspberry Pi" microprocessor.


# how to use a GPU in windows:
1. install Visual Studio Community version. during the installation choose "Desktop development with C++"
2. set the NVIDIA driver for your GPU
3. install CUDA Toolkit
4. install CUDA DNN should be ths same version as the toolkit
5. install torch (should be compatible with CUDA)  
    YOLO with GPU tutorial:  
    https://www.youtube.com/watch?v=WgPbbWmnXJ8&list=PL8M75DUkymbBjvikY8-BDVSPi6s4W9xhL&index=2&t=4097s









