from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import NotAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import User, Item
from .serializer import UserSerializer, ItemSerializer
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated


# Create your views here.

# class UserApi(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [AllowAny]

#     def get(self, request):
#         user = request.user
#         if not user.is_authenticated:
#             raise NotAuthenticated()
#         return Response({
#             "userName":user.userName,
#             "firstName":user.firstName,
#             "lastName":user.lastName,
#             "email":user.email,
#             "password":user.password,
#         })
    
#     def post(self, request):
#         username = request.data.get("username","")
#         password = request.data.get("password","")

#         if(username and password):
#             if User.objects.filter(username=username).exists():
#                 return Response({
#                     "error" : "A user with username exists",
#                 }, status=401)
#             user = User.objects.create(username=username, password=password)
#             refresh = RefreshToken.for_user(user)
#             return Response

class CreateItem(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ItemList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

class ItemDetail(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_item_by_pk(self,pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return None
    
        
    def put(self, request, pk):
        item  = self.get_item_by_pk(pk)
        if not item:
            return Response({'error': 'item does not exist!'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ItemSerializer(Item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        item = self.get_item_by_pk(pk)
        if not item:
            return Response({'error': 'item does not exist!'}, status=status.HTTP_404_NOT_FOUND)
        
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Register(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data.copy()  # Make a copy of the request data
        if 'password' in data:
            data['password'] = make_password(data['password'])  # Hash the password
        
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class UserListView(generics.ListAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]


    queryset = User.objects.all()
    serializer_class = UserSerializer

class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        if email is None or password is None:
            return Response({'detail': 'Please provide both email and password.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not check_password(password, user.password):
            return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)

