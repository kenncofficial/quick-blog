from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from blog.models import About, Roles, BlogPost
from portfolio.models import Portfolio_Post
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
class HomeView(ListView):
    model = Portfolio_Post
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["BlogPosts"] = BlogPost.objects.all().order_by('-date_posted')[:3]
        context["Portfolio_Posts"] = Portfolio_Post.objects.all()[:4]
        context["Abouts"] = About.objects.all()
        return context
  
class AboutView(ListView):
    model = About
    template_name = 'about.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutView, self).get_context_data(*args, **kwargs)
        context["Roles"] = Roles.objects.all()
        return context
    

class WorkView(ListView):
    model= Portfolio_Post
    template_name = 'work.html'
    paginate_by = 12
    

