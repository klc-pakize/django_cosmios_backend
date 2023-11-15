from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

from dj_rest_auth.serializers import TokenSerializer

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True,  validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
        style = {"input_type": "password"}
    )

    password2 = serializers.CharField(
        write_only = True,
        required = True,
        style = {"input_type": "password"}
    )

    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password2",
            "token",
        )

    def get_token(self, obj):
        token = Token.objects.get(user=obj)
        return token.key

    def validate_username(self, value):
        if value == "admin":
            raise serializers.ValidationError("Kullanıcı adı admin olamaz!!!")
        return value
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                "message": "Password fields didn't mach."
            })
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        
        return user
    
class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email")

class CustomTokenSerializer(TokenSerializer):
    user = UserTokenSerializer(read_only=True)

    class Meta:
        model = Token
        fields = ("key", "user")