from datetime import timedelta
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Category,MenuItem,Booking
class LittleLemonAPITests(APITestCase):
    def setUp(self):
        self.category=Category.objects.create(title="Mains",slug="mains")
        MenuItem.objects.create(title="Lemon Pasta",price="12.50",category=self.category)
        self.user=get_user_model().objects.create_user(username="tester",password="Testpass123")
    def test_menu_list(self):
        self.assertEqual(self.client.get("/api/menu-items/").status_code,status.HTTP_200_OK)
    def test_menu_write_requires_authentication(self):
        r=self.client.post("/api/menu-items/",{"title":"Soup","price":"5.00","category_id":self.category.id},format="json")
        self.assertEqual(r.status_code,status.HTTP_401_UNAUTHORIZED)
    def test_registration_returns_token(self):
        r=self.client.post("/api/registration/",{"username":"newuser","password":"Password123","email":"new@example.com"},format="json")
        self.assertEqual(r.status_code,status.HTTP_201_CREATED); self.assertIn("token",r.data)
    def test_booking_create(self):
        r=self.client.post("/api/bookings/",{"name":"Taylor","no_of_guests":2,"booking_date":(timezone.now()+timedelta(days=2)).isoformat()},format="json")
        self.assertEqual(r.status_code,status.HTTP_201_CREATED); self.assertEqual(Booking.objects.count(),1)
    def test_booking_guest_validation(self):
        r=self.client.post("/api/bookings/",{"name":"Taylor","no_of_guests":0,"booking_date":(timezone.now()+timedelta(days=2)).isoformat()},format="json")
        self.assertEqual(r.status_code,status.HTTP_400_BAD_REQUEST)
