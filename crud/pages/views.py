from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Crud
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    # post= get_object_or_404(Crud,id=id) 
    crud = Crud.objects.all()
    context={
        'crud':crud,
        
    }
    return render(request, 'index.html',context)



def delete(request, id):
    
   
    post = get_object_or_404(Crud, id=id)
    post.delete()
    return redirect("index")

    
def edit(request, id):
    
    
    return render(request, 'index.html')