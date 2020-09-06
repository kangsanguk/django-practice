from django.shortcuts import render

def ranking(request):
    return render(request, 'ranking.html')

def signup(request):
    return render(request, 'signup.html')