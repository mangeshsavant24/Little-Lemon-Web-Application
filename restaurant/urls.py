from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import home,MenuItemViewSet,CategoryViewSet,BookingListCreateView,BookingDetailView,RegistrationView,CurrentUserView
router=DefaultRouter()
router.register("api/menu-items",MenuItemViewSet,basename="menu-item")
router.register("api/categories",CategoryViewSet,basename="category")
urlpatterns=[path("",home,name="home"),path("",include(router.urls)),path("api/bookings/",BookingListCreateView.as_view()),path("api/bookings/<int:pk>/",BookingDetailView.as_view()),path("api/registration/",RegistrationView.as_view()),path("api/me/",CurrentUserView.as_view())]
