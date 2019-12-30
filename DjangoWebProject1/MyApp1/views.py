from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "MyApp1/index.html",
        {
            "title": "Hello Django",
            "message": "Reljod T. Oreta is learning Django!",
            "content": " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def about(request):

    return render(
            request,
            "MyApp1/about.html",
            {
                "title": "About MyApp1",
                "content": "Example app page for Django."
            }
        
        )