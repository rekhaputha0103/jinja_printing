from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'name':'Kalyani','a':19}
    return render(request,'conditions.html',d)