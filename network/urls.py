from django.urls import path

from network.apps import NetworkConfig
from network.views import CompanyDetailAPIView, CompanyCreateAPIView, \
    CompanyUpdateAPIView, CompanyListAPIView, CompanyDeleteAPIView

app_name = NetworkConfig.name

urlpatterns = [
    path("company/<int:pk>/", CompanyDetailAPIView.as_view(), name="company-detail"),
    path("delete/company/<int:pk>/", CompanyDeleteAPIView.as_view(), name="company-delete"),
    path("companies/", CompanyListAPIView.as_view(), name="company-list"),
    path("company/", CompanyCreateAPIView.as_view(), name="company-create"),
    path("update/company/<int:pk>/", CompanyUpdateAPIView.as_view(), name="company-update"),
]
