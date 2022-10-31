from .models import Booking, Flight
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from flights.models import Flight, Booking
from .serializers import FlightListSerializer, BookingListSerializer, BookingDetailSerializer, BookingCreateSerializer


class FlightView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

class BookingView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer    


class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'

class BookingCreateView(CreateAPIView):
    serializer_class = BookingCreateSerializer


class BookingUpdateView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'


class BookingDeleteView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer 
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'
    