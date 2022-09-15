from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request,'my_tmp/dashboard.html', context)

# Create your views here.
def signin(request):
    context = {}
    return render(request,'my_tmp/sign-in.html', context)

def signup(request):
    context = {}
    return render(request,'my_tmp/sign-up.html', context)