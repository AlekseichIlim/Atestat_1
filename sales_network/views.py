from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView

from sales_network.models import NetworkLink
from sales_network.serializers import NetworkLinkSerializer, NetworkLinkWithoutArrearsField


class NetworkLinkCreateAPIView(CreateAPIView):
    """Создание объекта сети"""

    serializer_class = NetworkLinkSerializer


class NetworkLinkListAPIView(ListAPIView):
    """Просмотр списка объектов сети"""

    serializer_class = NetworkLinkSerializer
    queryset = NetworkLink.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['country']


class NetworkLinkRetrieveAPIView(RetrieveAPIView):
    """Просмотр объекта сети"""

    serializer_class = NetworkLinkSerializer
    queryset = NetworkLink.objects.all()


class NetworkLinkUpdateAPIView(UpdateAPIView):
    """Изменение объекта сети"""

    serializer_class = NetworkLinkWithoutArrearsField
    queryset = NetworkLink.objects.all()
    # permission_classes = (IsOwnerPermission,)


class NetworkLinkDestroyAPIView(DestroyAPIView):
    """Удаление объекта сети"""

    serializer_class = NetworkLinkSerializer
    queryset = NetworkLink.objects.all()
