from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, CreateAPIView, UpdateAPIView

from network.models import Company
from network.permissions import IsActiveUser
from network.serializers import CompanyDetailSerializer, CompanySerializer, CompanyUpdateSerializer


class CompanyDetailAPIView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer
    permission_classes = (IsActiveUser, )


class CompanyDeleteAPIView(DestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsActiveUser, )


class CompanyListAPIView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('contacts__country', )
    permission_classes = (IsActiveUser, )


class CompanyCreateAPIView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsActiveUser, )


class CompanyUpdateAPIView(UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyUpdateSerializer
    permission_classes = (IsActiveUser, )
