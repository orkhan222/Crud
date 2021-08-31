
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Crud
from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from .models import *
from .forms import *
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

    
def create(request):
    form = IndexForm()
    if request.method == 'POST':
        form = IndexForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    context = {
        'form' : form
    }
    return render (request,'create.html',context)


def update(request,id):
    index = Crud.objects.get(id=id)
    form = IndexForm(instance=index)
    if request.method == 'POST':
        form = IndexForm(request.POST,instance=index)
        if form.is_valid():
            form.save()
        return redirect('index')
    context = {
        'form' : form
    }
    return render (request,'create.html',context)