from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("MERHABA DJANGO")

def home2(request):
    return HttpResponse("MERHABA COSMİOS YAZILIM AKADEMİ")