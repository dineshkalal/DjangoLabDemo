from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request,'welcome.html')

def showImg(request):
	return render(request,'demo.html')
def showlorem(request):
	return render(request,'demo2.html')