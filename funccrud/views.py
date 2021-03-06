from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog

def welcome(request):
    return render(request, 'funccrud/index.html')

def detail(request,pk):
    details=get_object_or_404(Blog, pk=pk)
    return render(request, 'funccrud/detail.html', {'details':details})
    

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'funccrud/funccrud.html', {'blogs':blogs})

def create(request): #역할 1. 새로운 블로그 글 저장POST   2. 글쓰기 페이지를 띄워줌GET(즉!=POST)
    if request.method == 'POST':
        form_content = NewBlog(request.POST)
        if form_content.is_valid:
            post = form_content.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form_content = NewBlog()
        return render(request, 'funccrud/new.html', {'formK':form_content})


def update(request, pk): #어떤 블로그 수정할지 객체 가져오기, 해당하는 블로그 객체의 입력공간
    blog = get_object_or_404(Blog, pk=pk)
    form_content = NewBlog(request.POST, instance=blog)
    if form_content.is_valid():
        form_content.save()
        return redirect('home')
    return render(request, 'funccrud/new.html', {'formK':form_content})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')
