from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics,permissions,viewsets,status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category,MenuItem,Booking
from .serializers import CategorySerializer,MenuItemSerializer,BookingSerializer
User=get_user_model()
def home(request): return render(request,"restaurant/index.html")
class RegistrationView(APIView):
    permission_classes=[permissions.AllowAny]; authentication_classes=[]
    def post(self,request):
        username=request.data.get("username","").strip(); password=request.data.get("password",""); email=request.data.get("email","").strip()
        if not username or not password: return Response({"detail":"username and password are required."},status=400)
        if len(password)<8: return Response({"password":["Password must contain at least 8 characters."]},status=400)
        if User.objects.filter(username=username).exists(): return Response({"username":["Username already exists."]},status=400)
        user=User.objects.create_user(username=username,password=password,email=email); token,_=Token.objects.get_or_create(user=user)
        return Response({"id":user.id,"username":user.username,"email":user.email,"token":token.key},status=201)
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset=MenuItem.objects.select_related("category").all(); serializer_class=MenuItemSerializer
    search_fields=["title","category__title"]; ordering_fields=["title","price"]; filterset_fields=["featured","category__slug"]
class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all(); serializer_class=CategorySerializer
class BookingListCreateView(generics.ListCreateAPIView):
    queryset=Booking.objects.select_related("user").all(); serializer_class=BookingSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self,serializer): serializer.save(user=self.request.user if self.request.user.is_authenticated else None)
class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Booking.objects.select_related("user").all(); serializer_class=BookingSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
class CurrentUserView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request): return Response({"id":request.user.id,"username":request.user.username,"email":request.user.email})
