from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, CreateAPIView, UpdateAPIView

from network.models import Company
from network.serializers import CompanyDetailSerializer, CompanySerializer, CompanyUpdateSerializer


class CompanyDetailAPIView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer


class CompanyDeleteAPIView(DestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyListAPIView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('contacts__country', )


class CompanyCreateAPIView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyUpdateAPIView(UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyUpdateSerializer
