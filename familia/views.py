from django.shortcuts import render
from .models import Informacion


def index(request):
    informaciones=Informacion.objects.all()
    ctx = {'informaciones': informaciones}
    return render(request,"familia/index.html", ctx)
    

