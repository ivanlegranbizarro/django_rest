from rest_framework import serializers
from django.core.validators import MaxLengthValidator, MinLengthValidator

from accounts.models import User


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, validators=[MinLengthValidator(6), MaxLengthValidator(12)]
    )

    class Meta:
        model = User
        fields = ["username", "email", "password", "birth_date"]

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
