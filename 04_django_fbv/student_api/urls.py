from django.urls import path

from .views import home, ogrincilerin_hepsini_getir, yeni_ogrenci_olusturma, tek_bir_ogrenci_görüntülme_getirme, var_olan_ogrenciyi_güuncelle, silinicek_ogrenci

urlpatterns = [
    path("home/", home),
    path("ogrencilerin_hepsi/", ogrincilerin_hepsini_getir),
    path("yeni_ogrenci/", yeni_ogrenci_olusturma),
    path("ogenci/<int:pk>/", tek_bir_ogrenci_görüntülme_getirme),
    path("ogrenci_güncel/<int:pk>/", var_olan_ogrenciyi_güuncelle),
    path("sil/<int:pk>/", silinicek_ogrenci),
]