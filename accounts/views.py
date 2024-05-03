from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from accounts.serializers import SignupSerializer

# Create your views here.


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
