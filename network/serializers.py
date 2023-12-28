from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, DateTimeField, IntegerField, DecimalField

from network.models import Company, Contact, Product


class CompanySerializer(ModelSerializer):
    created_at = DateTimeField(required=False, read_only=True)
    id = IntegerField(required=False, read_only=True)

    class Meta:
        model = Company
        fields = "__all__"

    def validate(self, attrs):
        if attrs.get('company_type', None) == 'Factory' and attrs.get('supplier', False):
            raise ValidationError('У завода-изготовителя нет поставщика готовой продукции')

        if attrs.get('company_type', None) == 'Factory' and attrs.get('indebtedness', False):
            raise ValidationError('У завода-изготовителя не может быть задолженности перед поставщиком')

        return attrs


class CompanyUpdateSerializer(ModelSerializer):
    created_at = DateTimeField(required=False, read_only=True)
    id = IntegerField(required=False, read_only=True)
    indebtedness = DecimalField(read_only=True, required=False, max_digits=15, decimal_places=2)

    class Meta:
        model = Company
        fields = "__all__"


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class CompanyDetailSerializer(ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    customers = CompanySerializer(many=True, read_only=True)
    contacts = ContactSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = '__all__'
