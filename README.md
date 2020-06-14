# face_recognition
This repository contains the necessary actions required to run the face_recognition library of python.
### Installing Depedencies
#### Conda
##### Download the installer [here](https://www.anaconda.com/products/individual) and bash the file using

    bash Anaconda-latest-Linux-x86_64.sh    
##### Create a new environment

    conda create --name myenv
##### Activate the environment
    
    conda activate myenv
#### Python Packages 
##### Opencv
    
    pip install opencv-contrib-python
##### Numpy

    pip install numpy
##### face_recognition

    pip install face_recognition
There is an usual error of dlib for new users, for that, use the following and then run the above command

    sudo apt-get install build-essential cmake
    sudo apt-get install libgtk-3-dev
    sudo apt-get install libboost-all-dev
##### Pillow

    pip install Pillow
##### IPython

    pip install ipython
##### Pickle

    pip install pickle5
##### pandas

    pip install pandas

###### After all the dependencies are installed, open the notebook and run the code.
###### Note: Do not overwrite the known_faces.txt or known_faces.txt. Append the data onto it instead of overwriting it.
###### Note: This is compatible with python 3.6.10 and above.
Learn more about face_recognition [here](https://github.com/ageitgey/face_recognition)
