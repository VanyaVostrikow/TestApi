from rest_framework import serializers
from .models import CategoriesOfProducts, GroupsofProducts, Product
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

class COPSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CategoriesOfProducts
        fields = ("__all__")




class GOPSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupsofProducts
        fields = ('__all__')

        
class PSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('__all__')

        
    # id = serializers.IntegerField()
    # name = serializers.CharField(max_length=255)
    # seq = serializers.IntegerField()

    # def create(self, validated_data):
    #     return CategoriesOfProducts.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.seq = validated_data.get('seq', instance.seq)
    #     instance.save()
    #     return instance
    
    # def delete(self, instance):

        

