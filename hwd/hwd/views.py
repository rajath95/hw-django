from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response,render
from .models import Books,Feedback
from .forms import feedbackForm

def hello(request):
    return HttpResponse("hello")

def q_books(request):
    token={}
    token['books']=Books.objects.all()
    return render_to_response("books.html",token)

def feedback(request):
    if request.method=='POST':
        fdbk=feedbackForm(request.POST)
        if fdbk.is_valid():
            name = fdbk.cleaned_data['name']
            title=fdbk.cleaned_data['title']
            rating = fdbk.cleaned_data['rating']
            desc=fdbk.cleaned_data['desc']
            p = Feedback(name=name,title=title,rating=rating,desc=desc)
            p.save()

    else:
        fdbk=feedbackForm()
    return render(request,"feedback.html",{'form':fdbk})
