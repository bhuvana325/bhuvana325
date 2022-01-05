from rest_framework.serializers import ModelSerializer

from . import models
from .models import products


class productsSerializers(ModelSerializer):
    class Meta:
        model = products
        fields=['name','costperitem','stockquantity','volume']

