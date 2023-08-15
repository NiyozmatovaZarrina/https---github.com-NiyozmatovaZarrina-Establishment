from rest_framework import generics
from ..models import Name
from ..serializers import NameSerializer


class NameList(generics.ListCreateAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer

class NameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer

class NameByCategoryList(generics.ListAPIView):
    serializer_class = NameSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Name.objects.filter(category_id=category_id)

class NameByCityList(generics.ListAPIView):
    serializer_class = NameSerializer

    def get_queryset(self):
        city = self.kwargs['city']
        return Name.objects.filter(city=city)

class NameSearchByAddressList(generics.ListAPIView):
    serializer_class = NameSerializer

    def get_queryset(self):
        address = self.kwargs['address']
        return Name.objects.filter(address__icontains=address)

class NameSearchByNameList(generics.ListAPIView):
    serializer_class = NameSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Name.objects.filter(name__icontains=name)
    