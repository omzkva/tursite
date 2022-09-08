from rest_framework import viewsets
from .models import Region, Location, Route, Kind_transport, Food, Housing, Contact
from .serializers import FoodSerializer, HousingSerializer, Kind_transportSerializer, LocationSerializer, RegionSerializer, ContactSerializer, RouteSerializer

class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class LocationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class RouteViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class Kind_transportViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Kind_transport.objects.all()
    serializer_class = Kind_transportSerializer


class HousingViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Housing.objects.all()
    serializer_class = HousingSerializer


class FoodViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer