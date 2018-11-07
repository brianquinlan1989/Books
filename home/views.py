from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Topic
from .forms import TopicForm, BookForm

def say_hello(request):
    topics = Topic.objects.all()
    
    if "id" in request.GET:
        topic_id = request.GET["id"]
        books = Book.objects.filter(topic=topic_id)
    else:
        books = Book.objects.all()
   
    return render(request, "home/index.html", {'books':books, 'topics':topics})
    
def add_topic(request):
    form = TopicForm()
    return render(request, "home/add_topic.html", {"form": form})
    
def add_topic_for_real(request):
    form = TopicForm(request.POST)
    form.save()
    
    #----The below 4 lines does the same as the 2 above ---- 
    
    # topic_name = request.POST["name"]
    # t=Topic()
    # t.name=topic_name
    # t.save()
    
    return redirect("/")
    
def add_book(request):
    form = BookForm()
    return render(request, "home/add_book.html", {"form": form})
    
def add_book_for_real(request):
    form = BookForm(request.POST)
    form.save()
    
    return redirect("/")