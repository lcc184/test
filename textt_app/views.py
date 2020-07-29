from django.shortcuts import render
from textt_app.models import Goodtext
# Create your views here.
def index(request):
    good_list = Goodtext.objects.all()
    return render(request,"tett_app/index.html",{"good_list":good_list})