from django.shortcuts import render, HttpResponse
from django.views import View

class Sayhello(View):
    def get(self, request):
        return render(request, "mycars/bike.html")
#return HttpResponse("Hello, friend")
