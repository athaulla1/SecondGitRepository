from django.shortcuts import render
from django.http import HttpResponse
from .models import *



# Create your views here.
def index(request):
    data={'name':'Athaulla','hobby':'volleyball'}
    return render(request,'display/indexresponse.html',{'data1':data})
    #return HttpResponse(html)


def add(request):

    if request.method == "POST":
        #client : add(without data) --- send the html  -- form n1 and n2....submit (http://localhost:8000/add)
        math1 = Mymath()

        math1.number1 = int(request.POST["n1"])
        math1.number2 = int(request.POST["n2"])
        math1.result = math1.n1 + math1.n2

        data = {"mathobj1":math1}
        return render(request,"display/djangoaddresponse.html",{"response":data})
    else:  #without any data...
        return render(request,"display/djangoadd.html")
    #txt1 = "<html><body><h1> For Input {} , {} sum result is {} </h1> </body> </html>".format(n1,n2,res)
    #txt2 = "</h1> </body> </html>"
    #html = txt1+txt2


