from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# signup을 위해 auth라는 녀석 import
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            # 아이디가 중복되거나, 비밀번호가 다른 경우 가입이 되지 않음.
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, "signup.html", {"error" : "Username has already been taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                # 로그인시키고
                auth.login(request, user)
                # 다시 home으로 돌아가기
                return redirect('home')
        else:
            return render(request, "signup.html",{"error":"Passwords must match"} )
    # 실패하면 signup 페이지에 머물기
    return render(request, "signup.html")



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        redirect('home')
    return render(request, 'login.html')

    return render(request, "login.html")