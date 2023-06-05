from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import login, user_logged_in, authenticate, logout
from django.shortcuts import get_object_or_404
import json


class TokenSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']


class GetToken(viewsets.ViewSet):
    def create_user(self, request, *args, **kwsrgs):
        if request.body:
            body = json.loads(request.body)
            try:
                username = body['username']
                password = body['password']
                email = body['email']
            except Exception as e:
                return Response({'error':'check fields', 'error_except':str(e)})
            try:
                user = str(get_object_or_404(User, username=username))
                return Response({'error':'already exists'})
            except Exception as e:
                User.objects.create_user(username=username, email=email, password=password)
                user = str(get_object_or_404(User, username=username))
                return Response({'user':user})   
        else:
            return Response({'error':'empty request'}) 
    def gettoken(self, request, *args, **kwargs):
        login_check = True
        if request.body:
            login_check = False
            body = json.loads(request.body)
            try:
                try:
                    user1 = body['username']
                    try:
                        user = get_object_or_404(User, username=user1)
                    except Exception as e:
                        return Response({'error':str(e)})
                except:
                    user1 = body['email']
                    try:
                        user = get_object_or_404(User, email=user1)
                    except Exception as e:
                        return Response({'error':str(e)})
                    user1 = user.username
                password = body['password']
                try:
                    user = get_object_or_404(User, username=user1)
                except Exception as e:
                    return Response({'error':str(e)})
                check = user.check_password(password)
                user_log = authenticate(request, username=user1, password=password)
                if check is True:
                    try:
                        login(request, user_log)
                    except Exception as e:
                        return Response({'error':str(e)})
                else:
                    return Response({'error':'password is not correct'})
            except Exception as e:
                return Response({'error':'check fields', 'error_Except':str(e)})
        try:
            token = Token.objects.get_or_create(user=request.user)
        except Exception as e:
            return Response({"error401":"NotAuthorised", "solve":"put username/email&pass into body"})     
        serilizer = TokenSerilizer(instance=token[0])
        if login_check==False:
            logout(request)
        return Response({'token':serilizer.data})
    
    def logout(self, request):
        logout(request)
        
        return Response({'logout':'ok'})
    
    def login(self, request):
            token = str(request.headers['Authorization'])
            token = token.split(' ')[1]
            user = get_object_or_404(Token, key=token)
            user = user.user
            user = get_object_or_404(User, username=user)
            login(request,user=user)
            return Response({'logging':'Yeah'})
    
    def whoami(self, request):
        user = str(request.user)
        try:
            token = str(request.headers['Authorization'])
        except:
            token = 'notsend'    
        return Response({'user':user, 'token':token})
# Create your views here.
