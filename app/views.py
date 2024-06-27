from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'divya','age':22}
    return render(request,'jinja_print.html',context=d)

def ifelif(request):
    d={'name':'divya','age':39}
    return render(request,'ifelif.html',context=d)

def nestedif(request):
    d={'name':'divya','age':100}
    return render(request,'nestedif.html',d)
def forloop(request):
    d={'name':'divya','age':100}
    return render(request,'forloop.html',d)