from django.shortcuts import render,HttpResponseRedirect
from .form import UserForm
from .models import User
from django.contrib import messages


# This Function For Show data to template and Save data to database
def add_show(request):
    if request.method=='POST':
        fm=UserForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            ne=fm.cleaned_data['email']
            np=fm.cleaned_data['password']
            reg=User(name=nm,email=ne,password=np)
            reg.save()
            fm=UserForm()
            messages.success(request,"Data Added Successfully!!!")       
    else:
        fm=UserForm()
    stud = User.objects.all()
    return render(request,'app1/addshow.html',{'form':fm,'stu':stud,'message':messages})


# Delete Function 

def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        messages.success(request,"Deleted Successfully!!")
        return HttpResponseRedirect('/')
    return render(request,'app1/addshow.html',{'message':messages})


# This Funtion For Update And Edit 

def update_data(request, id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=UserForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Updated Successfully!!")
        else:
            messages.success(request,"Something is Wrong")
    else:
        pi=User.objects.get(pk=id)
        fm=UserForm(instance=pi)
    return render(request,'app1/update.html',{'form':fm,'message':messages})