from rest_framework import viewsets

from .models import Schedule
from .serializers import ScheduleSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.order_by("id")
    serializer_class = ScheduleSerializer
