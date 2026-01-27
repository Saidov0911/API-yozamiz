from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

# def homepage(request):
#     return render("Salom dunyo")
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutmeView(TemplateView):
    template_name = 'about.html'