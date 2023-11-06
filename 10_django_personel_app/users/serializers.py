from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True,required = True)
    first_name = serializers.CharField(required = True)


    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "password2",
            "first_name",
            "last_name",
            "email",
        )
    
# attrs = {
#             "username":"pakize",
#             "password":"Pakize123",
#             "password2": "Pakize123",
#             "first_name":"Pakize",
#             "last_name":"Kılıç",
#             "email":"pa3kize@gmail.com",
# }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"Error":"Your passwords didn't match."})
        
        return attrs
    
# validated_data = {
#             "username":"pakize",
#             "password":"Pakize123",
#             "password2": "Pakize123",
#             "first_name":"Pakize",
#             "last_name":"Kılıç",
#             "email":"pa3kize@gmail.com",
# }

    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user
    

    # def create(self, validated_data):
    #     user = User.objects.create(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name']
    #     )  # (**validated_data)

    #     user.set_password(validated_data['password'])
    #     user.save()

    #     return user