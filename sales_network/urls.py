from django.urls import path
from sales_network.apps import SalesNetworkConfig
from sales_network.views import NetworkLinkCreateAPIView, NetworkLinkListAPIView, NetworkLinkRetrieveAPIView, \
    NetworkLinkUpdateAPIView, NetworkLinkDestroyAPIView

app_name = SalesNetworkConfig.name

urlpatterns = [
    path("create/", NetworkLinkCreateAPIView.as_view(), name="link_create"),
    path("", NetworkLinkListAPIView.as_view(), name="links_list"),
    path("<int:pk>/", NetworkLinkRetrieveAPIView.as_view(), name="link_detail"),
    path("<int:pk>/update/", NetworkLinkUpdateAPIView.as_view(), name="link_update"),
    path("<int:pk>/delete/", NetworkLinkDestroyAPIView.as_view(), name="link_delete"),
]