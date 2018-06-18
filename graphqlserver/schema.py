import graphene
from graphene_django import DjangoObjectType

from .models import Customer, Device ,Product


class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer


class DeviceType(DjangoObjectType):
    class Meta:
        model = Device

class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class Query(object):
    all_customers= graphene.List(CustomerType)
    all_devices = graphene.List(DeviceType)
    all_products = graphene.List(ProductType)

    def resolve_all_customers(self, info, **kwargs):
        return Customer.objects.all()

    def resolve_all_devices(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Device.objects.select_related('customer_id').all()

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.select_related('customer_id').all()
