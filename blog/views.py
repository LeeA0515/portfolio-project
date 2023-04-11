from django.shortcuts import render
from .models import Blog
def bloghome(request):
    blog = Blog.objects

    return render(request, 'blog/bloghome.html/',{'blog':blog} )
