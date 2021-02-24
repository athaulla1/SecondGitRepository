from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *

# Create your views here.

def index(request):
    qs = Album.objects.all()
    print("Inside Views Display all Method")
    return render(request, 'music/index.html',{'qs':qs})  

    #return render(request, 'studapp/studresults.html',context={"qs":qs})
    
def indexlist(request):
    qs = Album.objects.all()
    print("Inside Views Display all Method")
    return render(request, 'music/indexlist.html',{'qs':qs})  

def search(request,albumid):
    
    try:
        qs = Song.objects.filter(album_id=albumid)  # dont use filter method....
    except Song.DoesNotExist:
        
	    raise Http404("Album doesnot Exist")
        #return render(request,'music/index.html', {'album':album})
    else:
        return render(request, 'music/detaillist.html',{'qs':qs})  


def delete(request):
    aid = int(request.POST['albumid'])
    arec = Album.objects.get(album_id=aid)

    arec.delete()
    print("Record deleted")
    


