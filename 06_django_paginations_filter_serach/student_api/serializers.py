import datetime
from rest_framework import serializers

from .models import Student, Path

# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=50)
#     number = serializers.IntegerField()
#     age = serializers.IntegerField()
    
    
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.age = validated_data.get('age', instance.age)
#         instance.save()
#         return instance
    

# validated_data = {
#     "last_name":"Şeker",
# }


class StudentSerializer(serializers.ModelSerializer):
    
    # bron_year = serializers.SerializerMethodField()  # read_only = True
    path = serializers.StringRelatedField() # read_only = True
    path_id = serializers.IntegerField()

    class Meta:
        model = Student
        # fields = "__all__"
        # exclude = ["number"]
        fields = ("id", "first_name", "last_name", "number", "path", "path_id")

    # def get_bron_year(self, student):
    #     current_time = datetime.datetime.now()
    #     return current_time.year - student.age



class PathSerializer(serializers.ModelSerializer):

    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Path
        fields = ("id", "name","students")