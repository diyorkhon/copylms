from django.shortcuts import render
from django.views.generic import TemplateView , ListView
from .models import Post
# Create your views here.
class Homepageview(ListView):
     model=Post
     template_name = "home.html"


class AboutPageViews(TemplateView):
     template_name = "about.html"