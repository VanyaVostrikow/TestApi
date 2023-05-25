from django.db import models

class CategoriesOfProducts(models.Model):
    id = models.AutoField('id', primary_key=True, )
    name = models.CharField('name')
    seq = models.IntegerField('seq')

class GroupsofProducts(models.Model):
    id = models.AutoField('id',primary_key=True)
    category_id = models.ForeignKey(CategoriesOfProducts, on_delete = models.CASCADE, null=True, blank=True)
    name = models.CharField('name')
    description = models.CharField('description')
    seq = models.IntegerField('seq')

class Product(models.Model):
    id = models.AutoField('id', primary_key=True)
    group_id = models.ForeignKey(GroupsofProducts, on_delete=models.CASCADE, null=True, blank=True) 
    name = models.CharField('name')
    price = models.FloatField('price')
    hidden = models.BooleanField('hiddeen')   
# Create your models here.
