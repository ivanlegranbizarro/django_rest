from rest_framework import serializers
from rest_framework.authtoken.models import Token

from accounts.models import User


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password", "birth_date"]
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 6, "max_length": 12}
        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()

        Token.objects.create(user=user)

        return user
