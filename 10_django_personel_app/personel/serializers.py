from django.utils.timezone import now

from rest_framework import serializers

from .models import Department, Personnel


class DepartmanSerializer(serializers.ModelSerializer):

    personel_count = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = "__all__"


    def get_personel_count(self, derpartman_objesi):
        return derpartman_objesi.personnel_set.count()
    

class PersonnelSerializer(serializers.ModelSerializer):
    
    department = serializers.StringRelatedField()  # read_only
    department_id = serializers.IntegerField()
    user = serializers.StringRelatedField()
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = Personnel
        fields = "__all__"


# validated_data = {
#         "first_name": "Sinem",
#         "last_name": "ŞEKER",
#         "title": "3",
#         "gender": "F",
#         "salary": 70000000,
#         "department": 4,
#         "user": 1
#     }

    def get_days_since_joined(self, personnel_objesi):
        return (now() - personnel_objesi.start_date).days

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        personnel = Personnel.objects.create(**validated_data)
        return personnel