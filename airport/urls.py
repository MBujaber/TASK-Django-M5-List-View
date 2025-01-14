"""airport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from flights.views import FlightView, BookingView, BookingDetailView, BookingUpdateView, BookingDeleteView, BookingCreateView
from users.views import UserCreateAPIView, UserLoginAPIView 

urlpatterns = [
    path("admin/", admin.site.urls),
    path('flight/', FlightView.as_view(), name='flight-list'),
    path('flight/booking/', BookingView.as_view(), name='bookings-list'),
    path('flight/booking/create/', BookingCreateView.as_view(), name='book-flight'),
    path('flight/booking/<int:booking_id>/', BookingDetailView.as_view(), name='booking-details'),
    path('flight/booking/update/<int:booking_id>/', BookingUpdateView.as_view(), name='update-booking'),
    path('flight/booking/delete/<int:booking_id>/', BookingDeleteView.as_view(), name='cancel-booking'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    
]

