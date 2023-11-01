from django.urls import path, include

from .views import (
    #!########################## FUNCTİON BASED VİEW IMPORT ##########################
    home, 
    ogrincilerin_hepsini_getir, 
    yeni_ogrenci_olusturma, tek_bir_ogrenci_görüntülme_getirme,
    var_olan_ogrenciyi_güuncelle, 
    silinicek_ogrenci,

    #!########################## CLASS BASED VİEW IMPORT ##########################
    #! APIVIEW
    StudentListCreate, 
    StudentDetail,

    #! GENERICAPIView and Mixins
    StudentGAV, 
    StudentDetailGAV,
    
    #! Concrete Views
    StudentCV,
    StudentDetailCV,

    #! ViewSets
    StudentMVS,
    PathMVS
    
    )

from rest_framework import routers

#! ViewSets
router = routers.DefaultRouter()
router.register("studentmvs", StudentMVS)  # studentmvs/  studentmvs/<int:pk>/
router.register("path", PathMVS)

urlpatterns = [
    #!########################## FUNCTİON BASED VİEW ENDPOİNT ##########################
    path("home/", home),
    path("ogrencilerin_hepsi/", ogrincilerin_hepsini_getir),
    path("yeni_ogrenci/", yeni_ogrenci_olusturma),
    path("ogenci/<int:pk>/", tek_bir_ogrenci_görüntülme_getirme),
    path("ogrenci_güncel/<int:pk>/", var_olan_ogrenciyi_güuncelle),
    path("sil/<int:pk>/", silinicek_ogrenci),


    #!########################## CLASS BASED VİEW ENDPOİNT ##########################

    #! APIVIEW
    path("students/", StudentListCreate.as_view()),
    path("students/<int:pk>/", StudentDetail.as_view()),

    #! GENERICAPIView and Mixins
    path("studentgav/", StudentGAV.as_view()),
    path("studentgav/<int:pk>/", StudentDetailGAV.as_view()),

    #! Concrete Views
    path("studencv/",StudentCV.as_view()),
    path("studencv/<int:pk>/",StudentDetailCV.as_view()),

    #! ViewSets
    # path("", include(router.urls)),
] + router.urls