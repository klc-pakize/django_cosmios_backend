from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer


class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]

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