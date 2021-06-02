from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from .models import Persons
# Create your views here.




def demo(request):
   obj=Place.objects.all()
   obj1 = Persons.objects.all()

   # name="kerala"
   return render(request,"index.html",{'result':obj,'result2':obj1})

# def addition(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    res=x+y
#
#    return render(request,"about.html",{'result':res})
# def contact(request):
#    return HttpResponse("this shows contact")
