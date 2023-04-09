from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts = [
        {
        'author' : 'Jason',
        'title' : 'My first site',
        'content' : 'Hi everyone',
        'date_posted' : 'March 8, 2023'
        },
        {
        'author' : 'Mich',
        'title' : 'Blog post',
        'content' : 'Am a mumu',
        'date_posted' : 'March 9, 2023'
        }
]

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
  
def about(request):
    return render(request, 'blog/about.html',{'title' : 'About'})