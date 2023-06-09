from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, mixins
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import COPSerializer, GOPSerializer, PSerializer
from .models import CategoriesOfProducts, GroupsofProducts, Product
from .pagination import DefaultPagination
from .deletecheck import DeleteCheck
from .SearchFilter import MySearch
from .multifilter import MultiFiltering
"""
Categories of Products UserViewset
"""
class KeyKey(TokenAuthentication):
    keyword = 'liwest'        

class COPViewSet(viewsets.GenericViewSet):    
    queryset = CategoriesOfProducts.objects.all()
    authentication_classes = [BasicAuthentication, KeyKey]
    permission_classes = [IsAuthenticated]
    serializer_class = COPSerializer
    pagination_class = DefaultPagination
       
    def mycreate(self, request):
        serializer = COPSerializer(data=request.data)
        seq = request.data.get('seq')
        serializer.is_valid(raise_exception=True)
        serializer.check_seq(seq)
        serializer.save()
        return Response({'answer':serializer.data})  

    def mydestroy(self, request, pk):        #Method DELETE
        check = DeleteCheck.COPcheck.check_delte(pk)
        if check == False:
            instance = get_object_or_404(CategoriesOfProducts, pk=pk)
            if instance:
                instance.delete()
                return Response({'answer':GOPSerializer(data=request.data).initial_data})
            else:
                return Response({'answer':'404notfound'})
        else:
            return Response({'error':'object has source'})
     
    def myupdate(self, request, pk, *args, **kwargs):            #Method PUT
        if not pk:
            return Response({'error':'404#NOT_FOUNDED', 'message':'Method PUT not allowed'})
        try:
            instance = CategoriesOfProducts.objects.get(pk=pk)
        except:
            return Response({'error':'404#NOT_FOUNDED', 'message':'Odject not founded'})
        serializer = COPSerializer(instance=instance, data=request.data, partial=True)
        serializer.check_seq(request.data.get('seq'))
        serializer.is_valid()
        serializer.save()
        return Response({'put':serializer.validated_data})
    
    def list(self, request, *args, **kwargs): #CUSTOM GET method (hidden-field exclude)
        list_queryset = MultiFiltering(request,self.queryset).get_filtered_queryset()
        if list_queryset.get('queryset') == None:
                if list_queryset.get('error') == None:
                    return Response({'error404':'not founded'})
                error = list_queryset.get('error')
                return Response({'error':error})
        list_queryset = list_queryset.get("queryset").order_by('seq')
        page = self.paginate_queryset(list_queryset) #реализация пагинации
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(list_queryset, many=True)
        return Response(serializer.data)
"""
Groups of Products UserViewset
"""
class GOPViewSet(viewsets.GenericViewSet):
    queryset = GroupsofProducts.objects.all()
    serializer_class = GOPSerializer
    pagination_class = DefaultPagination
    filter_backends = [filters.OrderingFilter]
    authentication_classes = [BasicAuthentication, KeyKey]

    def destroy(self, pk):        #method DELETE
        check = DeleteCheck.GOPcheck.check_delte(pk)
        if check == False:
            instance = get_object_or_404(GroupsofProducts, pk=pk)
            if instance:
                instance.delete()
                return Response({'answer':instance.name})
            else:
                return Response({'answer':'404notfound'})
        else:
            return Response({'error':'object has source'})
        
    def update(self, request, pk):     #method PUT
        if not pk:
            return Response({'error':'404#NOT_FOUNDED', 'message':'Method PUT not allowed'})
        try:
            instance = GroupsofProducts.objects.get(pk=pk)
        except:
            return Response({'error':'404#NOT_FOUNDED', 'message':'Odject not founded'})
        serializer = GOPSerializer(instance=instance, data=request.data, partial=True)
        serializer.check_seq()
        serializer.is_valid()
        serializer.save()
        return Response({'put':serializer.validated_data})
    
    def mycreate(self, request):
        serializer = GOPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'answer':serializer.data})
    
    def list(self, request): #CUSTOM GET method (hidden-field exclude)
        list_queryset = MultiFiltering(request,self.queryset).get_filtered_queryset()
        if list_queryset.get('queryset') == None:
                if list_queryset.get('error') == None:
                    return Response({'error404':'not founded'})
                error = list_queryset.get('error')
                return Response({'error':error})
        list_queryset = list_queryset.get("queryset")
        page = self.paginate_queryset(list_queryset) #реализация пагинации
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(list_queryset, many=True)
        return Response(serializer.data)
"""
Products VIEW
"""
class PViewSet(viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = PSerializer
    pagination_class = DefaultPagination
    filter_backends = [MySearch]
    authentication_classes = [BasicAuthentication, KeyKey]
    search_fields = ['=name']

    def update(self, request, pk):     #Method PUT
        if not pk:
            return Response({'error':'404#NOT_FOUNDED', 'message':'Method PUT not allowed'})
        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({'error':'404#NOT_FOUNDED', 'message':'Odject not founded'})
        serializer = PSerializer(instance=instance, data=request.data, partial=True)
        
        serializer.is_valid()
        serializer.save()
        return Response({'put':serializer.validated_data})
    
    def list(self, request): #CUSTOM GET method (hidden-field exclude)
        list_queryset = MultiFiltering(request,self.queryset).get_filtered_queryset()
        if list_queryset.get('queryset') == None:
                if list_queryset.get('error') == None:
                    return Response({'error404':'not founded'})
                error = list_queryset.get('error')
                return Response({'error':error})
        list_queryset = list_queryset.get("queryset")
        out_queryset = []
        for i in range(len(list_queryset)):
            if list_queryset[i].hidden == False:
                out_queryset.append(list_queryset[i])
        admincheck=request.user.is_superuser #отображать скрытые товары админу
        if admincheck == True:
            out_queryset = list_queryset
        page = self.paginate_queryset(out_queryset) #реализация пагинации
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(out_queryset, many=True)
        return Response(serializer.data)
    
    def mycreate(self, request, *args, **kwargs):
        serializer = PSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'answer':serializer.data})

    def mydestroy(self, request, pk, *args, **kwargs):        #Method DELETE
        instance = get_object_or_404(Product, pk=pk)
        if instance:
            instance.delete()
            return Response({'answer':PSerializer(data=request.data).initial_data})
        else:
            return Response({'answer':'404notfound'})
