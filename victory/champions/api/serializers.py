from rest_framework import serializers
from champions.models import Product
from rest_framework.validators import UniqueValidator

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) # cannot be modified
    name = serializers.CharField(max_length=100,validators=[UniqueValidator(queryset=Product.objects.all())])
    price = serializers.IntegerField(default=0)
    image = serializers.ImageField(allow_null=True, allow_empty_file=True)  # to be solved
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


    def create(self, validated_data):
        print(validated_data)
        print('here in create')
        return Product.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.price= validated_data.get('price')
        instance.image = validated_data.get('image')
        instance.save()
        return  instance
