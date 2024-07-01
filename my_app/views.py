from django.shortcuts import render
from django.views.generic import View
from my_app.forms import Register
# Create your views here.

class Helloview(View):
    def get(self,request):
        
        return render(request,"indx.html")
    
    def post(self,request):
        print(request.POST)
        
        return render(request,"indx.html")


class Add(View):
    def get(self,request):
        
        return render(request,"calculator.html")
    
    def post(self,request):
        print(request.POST)
        
        num1=int(request.POST.get("num1"))
        num2=int(request.POST.get("num2"))
        res=num1+num2
        print(res)
        
        return render(request,"calculator.html",{"result":res})
    
    
class Subtraction(View):
    def get(self,request):
        
        return render(request,"calculator.html")
    
    def post(self,request):
        print(request.POST)
        
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        result=n1-n2
        print(result)
        
        return render(request,"calculator.html",{"result":result})

class Multiplication(View):
    def get(self,request):
        
        return render(request,"calculator.html")
    
    def post(self,request):
        print(request.POST)
        
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1*n2
        print(res)
        
        return render(request,"calculator.html",{"result":res})
        
class Registration(View):
    def get(self,request):
        form=Register()
        
        return render(request,"register.html",{"form":form})  
    
    def post(self,request):
        print(request.POST) 
        form=Register(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        form=Register()
        return render(request,"register.html",{"form":form}) 


class Calc_view(View):
    
    def get(self,request):
        form=Register()
        return render(request,"calculator.html",{"form":form})
    
    def post(self,request):
        
        form=Register(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            num1=int(form.cleaned_data.get("num1"))
            num2=int(form.cleaned_data.get("num2"))
            res=num1+num2
            form=Register()
            return render(request,"calculator.html",{"result":res,"form":form})
        else:
            return render(request,"calculator.html")
    
        