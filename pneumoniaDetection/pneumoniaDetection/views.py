from django.shortcuts import render, HttpResponse, redirect
import requests
from django.core.files.storage import FileSystemStorage

def index(req):
    return render(req, 'HTML/index.html')


def predict(req):
    if req.method == "POST":
        #file in the sense its image obtained from the form
        fileObj = req.FILES['imgpath']
        fs = FileSystemStorage()
        filePathName = fs.save(fileObj.name,fileObj)
        filePathName = fs.url(filePathName)
        context={'imgg':filePathName}


        return render(req, 'HTML/result.html',context)