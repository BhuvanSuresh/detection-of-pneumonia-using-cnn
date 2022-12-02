from django.shortcuts import render, HttpResponse, redirect
import requests
from django.core.files.storage import FileSystemStorage

#below imports are for cnn model
import numpy as np
import matplotlib.pyplot as plt 
import os
from PIL import Image
import keras
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
import keras.utils as image
#from sklearn.metrics import classification_report, confusion_matrix

def index(req):
    return render(req, 'HTML/index.html')


def predict(req):
    if req.method == "POST":
        #file in the sense its image obtained from the form
        fileObj = req.FILES['imgpath']
        fs = FileSystemStorage()
        filePathName = fs.save(fileObj.name,fileObj)
        filePathName = fs.url(filePathName)
        #context={'imgg':filePathName}

        #load the model
        load_model = keras.models.load_model("cnnmodels\saved_cnn_model")
        #print(load_model.summary())
        print(filePathName)
        filePathName = filePathName.replace("/","\\")
        print(str(os.getcwd())+str(filePathName))
        s = str(os.getcwd())+str(filePathName)
        test_image = image.load_img(s, target_size = (64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = load_model.predict(test_image)
        res = int(result.round()[0][0])
        print(res)
        if(res==0):
            context={"result":"Normal"}
            return render(req, 'HTML/normal.html',context)
        else:
            context={"result":"Pneumoic"}            
            return render(req, 'HTML/pneumoic.html',context)