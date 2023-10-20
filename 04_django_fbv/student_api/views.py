from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student

from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
#!########################## FUNCTİON BASED VİEW ##########################
@api_view(['GET'])  # == @api_view() 
def home(request):
    return Response({
        "home":"Home Page"
    })


"""
HTTP METHOD
1- GET=> (DB den verileri çağırmamı, public işlem herkes)
2- POST => (DB de yeni obje create, pravite)
3- PUT => (DB var obje update, pravite)
4- DELETE => (DB de obje siler, pravite)
5- PATCH => (DB var obje update, pravite)
"""

@api_view(['GET'])
def ogrincilerin_hepsini_getir(request):   # students
    orm_sorgusu_ile_cekilen_queryset_verileri = Student.objects.all()
    data_tipini_degistirme = StudentSerializer(orm_sorgusu_ile_cekilen_queryset_verileri, many = True)
    return Response(data_tipini_degistirme.data)


@api_view(['POST'])
def yeni_ogrenci_olusturma(request):
    gelen_ogrenci_datasini_degistir = StudentSerializer(data=request.data)
    if gelen_ogrenci_datasini_degistir.is_valid():
        gelen_ogrenci_datasini_degistir.save()
        return Response(gelen_ogrenci_datasini_degistir.data, status=status.HTTP_201_CREATED)
    return Response(gelen_ogrenci_datasini_degistir.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def tek_bir_ogrenci_görüntülme_getirme(request, pk):
    # try:
    #     istenilen_ogrenciyi_db_orm_getir = Student.objects.get(id=pk)
    #     data_cevirmek_icin = StudentSerializer(istenilen_ogrenciyi_db_orm_getir)
    #     return Response(data_cevirmek_icin.data)
    # except:
    #     return Response({"message":"olmayan id girdin idnin kontorl"})

    istenilen_ogrenciyi_db_orm_getir = get_object_or_404(Student,id=pk)
    data_cevirmek_icin = StudentSerializer(istenilen_ogrenciyi_db_orm_getir)
    return Response(data_cevirmek_icin.data)


@api_view(['PUT'])
def var_olan_ogrenciyi_güuncelle(request, pk):
    eski_ogrenci = get_object_or_404(Student, id=pk)
    cevirici = StudentSerializer(instance=eski_ogrenci, data=request.data)
    if cevirici.is_valid():
        cevirici.save()
        return Response(cevirici.data, status=status.HTTP_201_CREATED)
    return Response(cevirici.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def silinicek_ogrenci(request, pk):
    delete_ogrenci = get_object_or_404(Student, id=pk)
    delete_ogrenci.delete()
    message = {
        "message":f"{pk} idsisne sahip öğrenci silindi"
    }
    return Response(message)