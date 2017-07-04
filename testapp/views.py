# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .serializers import *
from .models import Profile


# Create your views here.


from django.http import HttpResponse




class SignUpViewSet(viewsets.ModelViewSet):
	permission_classes = (AllowAny,)
	queryset = User.objects.all()
	serializer_class = UserSerializer
	# filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
	# ordering_fields = ('user_id')
	# filter_fields = {
	# 		'user_id': ['exact'],
	# 	}


	# def get_queryset(self):
	# 	queryset = User.objects.all()
	# 	self.access_token()
	# 	# queryset = Token.objects.all()
	# 	return queryset

	# def access_token(self):
	# 	# import pdb;pdb.set_trace()
	# 	for user in User.objects.all():
	# 		token, created = Token.objects.get_or_create(user = user)
	# 	return 

	# def get_serializer_class(self):
	# 	import pdb;pdb.set_trace()
	# 	serializer_class = UserSerializer
	# 	return serializer_class