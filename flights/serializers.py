from rest_framework import serializers
from flights.models import Booking, Flight
from rest_framework_simplejwt.tokens import RefreshToken

class FlightListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'destination', 'time','price']

class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['flight', 'date', 'id']
        
        
class BookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'flight', 'date','passengers']

class BookingCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Booking
        fields = ['passengers', 'flight', 'date', 'user']



class BookingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['passengers', 'date']

