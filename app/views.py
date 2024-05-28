from django.shortcuts import render
from .models import Product , Textarea,Textarea1,slider2,slider1
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def product(request):
    template = loader.get_template('index.html')
    products = Product.objects.all()
    textareas = Textarea.objects.all()  # Corrected variable name
    textareas1 = Textarea1.objects.all()  # Corrected variable name
    sliders1=slider1.objects.all()
    sliders2=slider2.objects.all()
    return render(request, "index.html", {"products": products, "textareas": textareas,"textareas1": textareas1,"sliders1":sliders1,"sliders2":sliders2})



def login (request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render()) 



def form (request):
  template = loader.get_template('form.html')
  return HttpResponse(template.render()) 
  
#def index(request):
#    books = Book.objects.all()
#    context = {
#        'books': books
#    }
#    return render(request, 'index.html', context)