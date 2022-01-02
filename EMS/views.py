from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import employee_detail , salary_detail
import pandas as pd

def home(request):
    return render(request,'home.html')

def add(request):
    if request.method == "POST":
         nam =request.POST["a1"]
         DO  = request.POST["a2"]
         pos  =request.POST["a3"]
         bs   =int(request.POST["a4"])
         DOJ1 =request.POST["a5"]
         add =request.POST["a6"]
         employee_detail.objects.create(name = nam , DOB=DO , basic_pay=bs, DOJ=DOJ1 , address=add , position=pos)
         messages.info(request,'Record inserted successfully.')
         return redirect('add')
    else:
         return render(request,"result.html",{'A':True ,'B':False,'C':False,'D':False })


def Dshow(request):
    if request.method == "POST":
        code=request.POST["ds1"]
        if code=="all":
            temp=employee_detail.objects.all()
            res={'tt':temp , 'A':True}
            return render(request,"output.html",res)
        else:
            try:
               temp = employee_detail.objects.get(id=int(code))
               print(temp.name)
               res={'te': temp , 'A':False}
               return render(request,"output.html",res)
            except:
                return HttpResponse("No record Found for given Emoloyee Code. Please give another")
    else:    
        return render(request,"result.html",{'B':True ,'A':False,'C':False,'D':False })



def salary(request):
    if request.method == "POST":
        code =request.POST["s1"]
        yr   =request.POST["s2"]
        mon  =request.POST["s3"]
        wd   =int(request.POST["s4"])
        ewd  =int(request.POST["s5"])
        t=employee_detail.objects.get(id=int(code))
        nam=t.name
        bs=int(t.basic_pay)
        sal=(bs/wd)*ewd
        salary_detail.objects.create(Emp_code = code ,Name=nam,year = yr,month =mon,Number_of_working_days=wd,Employee_working_days=ewd,salary=sal)
        messages.info(request,'Salary updated successfully.')
        return redirect('salary')
    else:
        return render(request,"result.html",{'C':True ,'B':False,'A':False,'D':False })
    

def S_show(request):
    if request.method == "POST":
        code=request.POST["ss1"]
        if code=="all":
            temp=salary_detail.objects.all()
            res={'tt':temp,'A':True}
            return render(request,"outt.html",res)
           
        else:
            try:
                tempt = employee_detail.objects.get(id=int(code))
                temp=salary_detail.objects.filter(Emp_code=int(code))
                res={'te':temp,'A':False}
                return render(request,"outt.html",res)
            except:
                return HttpResponse("No record Found for given Emoloyee Code. Please give another")
            
    else:    
       return render(request,"result.html",{'D':True ,'B':False,'C':False,'A':False })
