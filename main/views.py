from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .models import posts
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView
from .forms import addpost
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.

def main(request):
    return render(request,'main/main.html')

class home(LoginRequiredMixin,ListView):
    redirect_field_name = 'Login'
    model=posts
    template_name='main/home.html'
    context_object_name='posts'
    ordering=['-Posted']

class Individual(LoginRequiredMixin,ListView):
    model=posts
    template_name='main/Individual.html'
    context_object_name='posts'


class add_post(LoginRequiredMixin,CreateView):
    model=posts
    template_name='main/add.html'    
    fields=['Title','Image','Content']

    def form_valid(self,form):
        form.instance.Author=self.request.user
        return super().form_valid(form)

class update_post(LoginRequiredMixin,UpdateView):
    model=posts 
    template_name='main/add.html'  

    def form_valid(self,form):
        form.instance.Author=self.request.user
        return super().form_valid(form)

class delete_post(LoginRequiredMixin,DeleteView):
    model=posts
    template_name='main/delete.html' 
    context_object_name='del'


@login_required    
def myposts(request):
    return render(request,'main/myposts.html',{'posts':posts.objects.all()})    