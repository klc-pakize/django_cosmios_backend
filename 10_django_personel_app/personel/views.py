from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Department, Personnel
from .serializers import DepartmanSerializer, PersonnelSerializer
from .permissions import IsStaffOrReadOnly, IsOwnerAndStaffOrReadOnly


class DepartmanListCreateAPIView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmanSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]


class DepartmentPersonnelView(ListAPIView):
    serializer_class = DepartmanSerializer
    queryset = Department.objects.all()
    
    def get_queryset(self):
        name = self.kwargs["department"]
        return Department.objects.filter(name__iexact=name)

class PersonnelListCreateAPIView(ListCreateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]

class PersonnelRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = [IsAuthenticated, IsOwnerAndStaffOrReadOnly]
