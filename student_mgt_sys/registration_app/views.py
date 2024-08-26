from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Datas

# Create your views here.

def home(request): # 127.0.0.1
  mydata=Datas.objects.all()
  if(mydata!=''):
    return render(request,"home.html",{'datas':mydata}) 
  else:
    return render(request,"home.html")

def addData(request): # 127.0.0.1/addData
  if request.method=='POST':
    name=request.POST['name']
    age=request.POST['age']
    sex=request.POST['sex'] 
    standard=request.POST['standard']
    percentage=request.POST['percentage']
    address=request.POST['address']

    obj1=Datas()
    obj1.Name=name 
    obj1.Age=age
    obj1.Sex=sex
    obj1.Standard=standard
    obj1.Percentage=percentage
    obj1.Address=address
    obj1.save()
    mydata=Datas.objects.all()
    return render(request,"home.html",{'datas':mydata})
  return render(request,"home.html")
  
def updateData(request,id):
  mydata=Datas.objects.get(id=id)
  if request.method=='POST':
    name=request.POST['name']
    age=request.POST['age']
    sex=request.POST['sex'] 
    standard=request.POST['standard']
    percentage=request.POST['percentage']
    address=request.POST['address']

    mydata.Name=name
    mydata.Age=age
    mydata.Sex=sex
    mydata.Standard=standard
    mydata.Percentage=percentage
    mydata.Address=address
    mydata.save()
    return redirect('home')

  return render(request,'update.html',{'data':mydata})

def deleteData(request,id):
  mydata=Datas.objects.get(id=id)
  mydata.delete()
  return redirect('home')