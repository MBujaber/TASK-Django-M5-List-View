from .models import Booking, Flight
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from flights.models import Flight, Booking
from .serializers import FlightListSerializer, BookingListSerializer, BookingDetailSerializer, BookingCreateSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsAuthor, CanEditBooking

class FlightView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer
    permission_classes = [IsAuthenticated]

class BookingView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer    
    permission_classes = [IsAuthenticated]

class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'
    permission_classes = [IsAuthenticated, IsAuthor]

class BookingCreateView(CreateAPIView):
    serializer_class = BookingCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookingUpdateView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'
    permission_classes = [IsAuthenticated, IsAuthor, CanEditBooking]


class BookingDeleteView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer 
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'
    permission_classes = [IsAuthenticated, IsAuthor, CanEditBooking]
    