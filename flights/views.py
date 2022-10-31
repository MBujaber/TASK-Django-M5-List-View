from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from flights.models import Flight
from .serializers import FlightListSerializer

class FlightView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

