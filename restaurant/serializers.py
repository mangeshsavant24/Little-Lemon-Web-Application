from rest_framework import serializers
from .models import Category,MenuItem,Booking
class CategorySerializer(serializers.ModelSerializer):
    class Meta: model=Category; fields=["id","title","slug"]
class MenuItemSerializer(serializers.ModelSerializer):
    category=CategorySerializer(read_only=True)
    category_id=serializers.PrimaryKeyRelatedField(source="category",queryset=Category.objects.all(),write_only=True)
    class Meta: model=MenuItem; fields=["id","title","price","featured","category","category_id"]
class BookingSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta: model=Booking; fields=["id","name","no_of_guests","booking_date","user"]; read_only_fields=["id","user"]
    def validate_no_of_guests(self,value):
        if not 1 <= value <= 20: raise serializers.ValidationError("Guests must be between 1 and 20.")
        return value
