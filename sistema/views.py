from django.shortcuts import render

# Create your views here.

# aqui irão ficar todas as views (controladores) referente ao sistema

def index(request):
    return render (
        request, 
        'sistema/index.html',
    )

