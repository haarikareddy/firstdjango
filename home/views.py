from django.shortcuts import render,redirect
from .forms import BookForms,SearchForm,modelBookForms
from home.models import Book
#from django.utils import timezone
from django.contrib import messages
# Create your views here.

def form_view(request):
    context=None
    msg=None
    form=None
    b=Book.objects.all()
    if request.method=='POST':
        form=BookForms(request.POST)
        if form.is_valid():
            b=Book.objects.create(
                name=form.cleaned_data.get('name'),
                purchase_date=form.cleaned_data.get('purchase_date'),
                author_name=form.cleaned_data.get('author'))
            b.save()
            msg='Book added successfully !!!'
        else:
            msg=form.errors
    #context={"msg":msg,"forms":form}
    else:
        form=BookForms()
    return render(request,'forms.html',{"msg":msg,"forms":form,'bk':b})

def model_form(request):  
    msg='' 
    if request.method=='POST':
        form=BookForms(request.POST)
        if form.is_valid():
            form.save()
            msg='Book added successfully !!!'
        else:
            msg=form.errors
    #context={"msg":msg,"forms":form}
    else:
        form=ModelBookForms()
    return render(request,'forms.html',{"msg":msg,"forms":form,'bk':b})

def html_form(request):
    value=''
    if request.method=='POST':
        value=request.POST.get('name')
    else:
        value='Wrong input'
    return render(request,'home2.html',{'value':value})

def booksearch(request):
    if request.method=='POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            q=form.cleaned_data.get('q')            
            book=Book.objects.filter(name__contains=q)
            return render(request,'showtables.html',{'book':book,'form':SearchForm()})
    else:
        form=SearchForm()
        book=Book.objects.all()
    return render(request,'showtables.html',{'book':book,'form':form})

def deletebook(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    messages.success(request,'Deleted #'+str(id)+'Successfully!!!')
    return redirect('/')

def editbook(request,id):
    book=Book.objects.get(id=id)
    if request.method=='POST':
        form=ModelBookForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Book Updated Successfully! ')
            return redirect('/')
    else:
        form=modelBookForms(instance=book)
    return render(request,'editbook.html',{'form':form})
#def home_view2(request):
 #   return render (request,'new.html')

#def home_view(request):
 #   return render (request,'home2.html')

#def design(request):
 #   return render (request,'home.html')

#def home_view1(request):
 #   return render (request,'signup.html')    

#def design1(request):
 #   return render (request,'login.html')

