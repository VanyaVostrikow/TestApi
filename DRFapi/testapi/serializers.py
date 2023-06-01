from rest_framework import serializers
from .models import CategoriesOfProducts, GroupsofProducts, Product
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

class COPSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesOfProducts
        fields = ("__all__")

    def check_seq(self,seq):
        queryset = CategoriesOfProducts.objects.all().order_by('seq')
        for i in range(len(queryset)):
            print(queryset[i], queryset[i].seq, seq,type(queryset[i]))
            if queryset[i].seq >= seq:

                queryset[i].seq += 1
                queryset[i].save()
            




class GOPSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupsofProducts
        fields = ('__all__')

    def check_seq(self,seq):
        queryset = GroupsofProducts.objects.all().order_by('seq')
        for i in range(len(queryset)):
            print(queryset[i], queryset[i].seq, seq,type(queryset[i]))
            if queryset[i].seq >= seq:

                queryset[i].seq += 1
                queryset[i].save()
        
class PSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('__all__')

        

        

