from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile
from rest_framework.authtoken.models import Token


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = 'mobile_number',


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ('url', 'username', 'email','password', 'profile')


    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        self.access_token(user)
        return user

    def access_token(self,user):
        # import pdb;pdb.set_trace()
        # for user in User.objects.all():
        token = Token.objects.create(user = user)
        return token