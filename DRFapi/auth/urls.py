
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from testapi import views
from testapi.views import *
from auth.views import *
from testapi.routers import MyRouter

urlpatterns = [
    #Admin
    path('admin/', admin.site.urls),
    #CategoryOfProducts
    path('gettoken/', GetToken.as_view({'get':'gettoken'})),
    path('logout/', GetToken.as_view({'get':'logout'})),
    path('login/', GetToken.as_view({'get':'login'})),
    path('whoami/', GetToken.as_view({'get':'whoami'})),
    path('create/', GetToken.as_view({'get':'create_user'})),
   
    
]
urlpatterns = format_suffix_patterns(urlpatterns)
