from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from .models import Books


def hello(request):
    return HttpResponse("hello")

def q_books(request):
    token={}
    token['books']=Books.objects.all()
    return render_to_response("books.html",token)
