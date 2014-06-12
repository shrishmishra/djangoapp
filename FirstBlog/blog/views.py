# Create your views here.

from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect
import time
from blog.models import posts
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger()

def home(request):
    if  request.user.is_authenticated(): 
        entries = posts.objects.all()
        return render_to_response('blog.html', {'posts' : entries.reverse() , 'a' : request.user.username , 'b' : 'fewf'})
    else:
        return render_to_response('index.html', {})

def blog(request):
    #entries = posts.objects.all()
    #return render_to_response('blog.html', {'posts' : entries.reverse()})
    return HttpResponseRedirect("/")
def savePost(request):
    text = request.POST.get('bodyText');
    newPost = posts();
    newPost.author = request.user.username;
    newPost.bodytext = text ; 
    newPost.timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    
    newPost.save()
    return HttpResponseRedirect("/")
    
    #entries = posts.objects.all()
   # return render_to_response('blog.html', {'posts' : entries , 'a' : request.user.username , 'b' : 'fewf'})

def likePost(request):
    id = request.POST.get('id');
    post = posts.objects.get(pk=id);
    post.likes += 1;
    post.save();
    return HttpResponseRedirect("/"); #redirect to homepage
    #entries = posts.objects.all()
    #return render_to_response('blog.html', {'posts' : entries , 'a' : request.user.username , 'b' : 'fewf'})


def deletePost(request):
    id = request.POST.get('id');
    post = posts.objects.get(pk=id)
    post.delete();
    return HttpResponseRedirect("/");
    #entries = posts.objects.all()
    #return render_to_response('blog.html', {'posts' : entries , 'a' : request.user.username , 'b' : 'fewf'})

def login(request):
    username = request.POST.get('email','');
    email = request.POST.get('email',''); 
    password = request.POST.get('password','');

    user = auth.authenticate(username=username, password=password);

    if user is not None:   
        auth.login(request, user)
        entries = posts.objects.all()
        return render_to_response('blog.html', {'posts' : entries , 'a' : username , 'b' : password})
    else:
        user = User.objects.create_user(username = username , email = email , password = password);
        user.save();
        user = auth.authenticate(username=username, password=password);
        entries = posts.objects.all()
        return render_to_response('blog.html', {'posts' : entries , 'a' : username , 'b' : password})

def boot(request):
    return render_to_response('boot.html',{});

def logout(request):
    auth.logout(request)
    return render_to_response('index.html',{}); 

def not_found(request):
    return render_to_response('404.html',{});
