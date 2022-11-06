from rest_framework.permissions import BasePermission
from .serializers import BookingCreateSerializer
from datetime  import date
from rest_framework.response import Response

class IsAuthor(BasePermission):
    message = "You must be the author of this article."

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.author == request.user


class CanEditBooking(BasePermission):
    message = "You are not authorized to edit booking"
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user == obj.user:
            current_time = date.today()
            departure = obj.date
            if (departure - current_time).days > 3:
                return True
            return False 
        return False