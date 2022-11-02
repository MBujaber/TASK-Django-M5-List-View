from rest_framework.permissions import BasePermission
from .serializers import BookingCreateSerializer
from datetime  import date
from rest_framework.response import Response
from django.utils.timezone import now

class IsAuthor(BasePermission):
    message = "You must be the author of this article."

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.author == request.user


class Iscanceled(BasePermission):
    message = "booking cannot be canceled or modified unless it's more than 3 days before the schedule time of departure."

    def is_end_date(self):
        date = BookingCreateSerializer.objects.filter(date=date)
        return now().date() > self.date and not self.complete


        # if date.today() < self.date:
        #     if not self.complete:
        #         return True
        #     else:
        #         pass
        # else:
        #     pass