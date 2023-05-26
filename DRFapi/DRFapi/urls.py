"""
URL configuration for DRFapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import Route, DynamicRoute
from rest_framework.urlpatterns import format_suffix_patterns
from testapi import views
from testapi.views import *
from auth.views import *

class MyRouter(routers.SimpleRouter):
    routes = [
        # List route.
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'list',
                'post': 'mycreate'
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
            
        ),
        # Dynamically generated list routes. Generated using
        # @action(detail=False) decorator on methods of the viewset.
        DynamicRoute(
            url=r'^{prefix}/{url_path}$',
            name='{basename}-{url_name}',
            detail=False,
            initkwargs={}
        ),
        # Detail route.
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={
                'get': 'retrieve',
                'put': 'myupdate',
                'patch': 'mypartial_update',
                'delete': 'mydestroy'
            },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Instance'}
        ),
        # Dynamically generated detail routes. Generated using
        # @action(detail=True) decorator on methods of the viewset.
        DynamicRoute(
            url=r'^{prefix}/{lookup}/{url_path}$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        ),
    ]

router = MyRouter()
router.register(r'product-categories', COPViewSet)
router.register(r'product-groups', GOPViewSet)
router.register(r'products', PViewSet)

urlpatterns = [
    #Admin
    path('admin/', admin.site.urls),
    #CategoryOfProducts
    path('api-v1/', include(router.urls)),
    path('api-v1/gettoken/', GetToken.as_view({'get':'create'})),
    path('api-v1/logout/', GetToken.as_view({'get':'logout'})),
    path('api-v1/login/', GetToken.as_view({'get':'login'})),
    path('api-v1/whoami/', GetToken.as_view({'get':'whoami'})),
    path('api-v1/create/', GetToken.as_view({'get':'create_user'})),
   
    
]
urlpatterns = format_suffix_patterns(urlpatterns)
