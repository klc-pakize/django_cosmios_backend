from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
#!########################## FUNCTİON BASED VİEW IMPORT ##########################
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#!########################## CLASS BASED VİEW IMPORT ##########################
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet





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


#!########################## CLASS BASED VİEW ##########################
#! APIVIEW
class StudentListCreate(APIView):
    def get(self, request):
        students = Student.objects.all()
        print("gelen student objeleri", students)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():  # == TRUE
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED)
        # == FALSE
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StudentDetail(APIView):

    def get(self,request, pk):
        istenilen_ogrenciyi_db_orm_getir = get_object_or_404(Student,id=pk)
        data_cevirmek_icin = StudentSerializer(istenilen_ogrenciyi_db_orm_getir)
        return Response(data_cevirmek_icin.data)


    def put(self,request, pk):
        eski_ogrenci = get_object_or_404(Student, id=pk)
        cevirici = StudentSerializer(instance=eski_ogrenci, data=request.data)
        if cevirici.is_valid():
            cevirici.save()
            return Response(cevirici.data, status=status.HTTP_201_CREATED)
        return Response(cevirici.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request, pk):
        delete_ogrenci = get_object_or_404(Student, id=pk)
        delete_ogrenci.delete()
        message = {
            "message":f"{pk} idsisne sahip öğrenci silindi"
        }
        return Response(message)


#! GENERICAPIView and Mixins
""" #? GenericApıView
# One of the key benefits of class-based views is the way they allow you to compose bits of reusable behavior. REST framework takes advantage of this by providing a number of pre-built views that provide for commonly used patterns.

# GenericAPIView class extends REST framework's APIView class, adding commonly required behavior for standard list and detail views.

#? Mixins
# - ListModelMixin
#     - list method
# - CreateModelMixin
#     - create method
# - RetrieveModelMixin
#     - retrieve method
# - UpdateModelMixin
#     - update method
# - DestroyModelMixin
#     - destroy method 
"""

class StudentGAV(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class StudentGAVList(mixins.ListModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class StudentDetailGAV(mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy( request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

#! Concrete Views
class StudentCV(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailCV(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


#! ViewSets

# - Django REST framework allows you to combine the logic for a set of related views in a single class, called a ViewSet. 

# - Typically, rather than explicitly registering the views in a viewset in the urlconf, you'll register the viewset with a router class, that automatically determines the urlconf for you.

# There are two main advantages of using a ViewSet class over using a View class.

#  - Repeated logic can be combined into a single class. In the above example, we only need to specify the queryset once, and it'll be used across multiple views.
#  - By using routers, we no longer need to deal with wiring up the URL conf ourselves.

# Both of these come with a trade-off. Using regular views and URL confs is more explicit and gives you more control. ViewSets are helpful if you want to get up and running quickly, or when you have a large API and you want to enforce a consistent URL configuration throughout.


class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def destroy(self, request, *args, **kwargs):
        # instance = self.get_object()
        # self.perform_destroy(instance)
        super().destroy(request, *args, **kwargs)
        message = {
            "message":"Öğrenci başarıyla silindi"
        }
        return Response(message,status=status.HTTP_204_NO_CONTENT)
    

class PathMVS(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer