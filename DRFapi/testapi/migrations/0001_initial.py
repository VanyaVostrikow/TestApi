# Generated by Django 4.2.1 on 2023-05-18 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesOfProducts',
            fields=[
                ('id', models.IntegerField(max_length=3, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(verbose_name='name')),
                ('seq', models.IntegerField(max_length=2, verbose_name='seq')),
            ],
        ),
        migrations.CreateModel(
            name='GroupsofProducts',
            fields=[
                ('id', models.IntegerField(max_length=2, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(verbose_name='name')),
                ('description', models.CharField(verbose_name='description')),
                ('seq', models.IntegerField(verbose_name='seq')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapi.categoriesofproducts')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(max_length=6, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(verbose_name='name')),
                ('price', models.FloatField(verbose_name='price')),
                ('hidden', models.BooleanField(verbose_name='hiddeen')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapi.groupsofproducts')),
            ],
        ),
    ]