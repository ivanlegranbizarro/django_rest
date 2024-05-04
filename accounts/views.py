from rest_framework.authtoken.models import Token
from rest_framework import generics, status
from django.contrib.auth import authenticate
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from accounts.serializers import SignupSerializer

# Create your views here.


class ListOfAllUsers(generics.GenericAPIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = SignupSerializer(instance=users, many=True)

        return Response(data=serializer.data, status=200)


class SignUpView(generics.GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request: Request) -> Response:
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()

            response = {"message": "User created successfully", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)

            response = {"message": "Login successfully", "token": token.key}

            return Response(data=response, status=status.HTTP_200_OK)

        return Response(
            data={"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
        )
