from django.shortcuts import render
from .models import Portfolio

# Create your views here.

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, "portfolio.html", {'portfolios':portfolios})  # 모든 객체 내용을 portfolio.html에 띄어주세요!