from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogPost

# Create your views here.
def home(request):
    blogs = Blog.objects
    # 블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    # 블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    # request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return 해준다.
    posts = paginator.get_page(page)
    return render(request, "home.html", {'blog' : blogs, 'posts' : posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, "detail.html", {"blog" : blog_detail})

def new(request): # new.html을 띄어주는 함수
    return render(request, "new.html", {})

def create(request): # 입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() # 객체를 데이터베이스에 저장해라! 객체.delete는 지우기!
    return redirect('/blog/' + str(blog.id)) # 다 처리한 후, 이 URL로 넘기세요.

    # redirect함수의 인자로 다른 url을 입력할 수 있다. 즉 프로젝트 외에 있는 URL을 부를 수 있다

def delete(request, blog_id):
    blog_delete = get_object_or_404(Blog, pk = blog_id)
    blog_delete.delete()
    return redirect('home')

# update.html로 가기 위한 함수
def update(request, blog_id):
    blog_update = get_object_or_404(Blog, pk = blog_id)
    return render(request, "update.html", {"blogupdate" : blog_update})


# 기존 글에 새롭게 덮어씌어야 한다.
# 기존 글에 해당하는 인스턴스를 가져와서 덮어씌어 주고 다시 db에 저장 
def updateSend(request, blog_id):
    update_post = get_object_or_404(Blog, pk = blog_id)
    update_post.title = request.GET["updatetitle"]
    update_post.body = request.GET["updatebody"]
    update_post.pub_date = timezone.datetime.now()
    update_post.save()
    return redirect('home')

def blogpost(request):
    if request.method == "POST":
        # POST 방식으로 요청이 들어왔을 때 실행할 코드 - form에 입력받는 데이터를 저장
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        # GET 방식으로 요청이 들어왔을 때 실행할 코드 - form을 보여주기
        form = BlogPost()
        return render(request, "new.html", {"form":form})

    

