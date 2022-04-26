from django.contrib.auth.models import User
from rest_framework import serializers
from floraison.models import item, order

### IMPORTANT: May need to change gitpod link each time a new workspace is opened ###
BASE_API_URL = 'https://8000-anthonydeva-djangobacke-pk8s8czgzh1.ws-us42.gitpod.io'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class ItemSerializer(serializers.ModelSerializer):
    ##ITS NICK! Add your variable here
    photo = serializers.SerializerMethodField('get_img_url')
    class Meta:
        model = item
        fields = '__all__'
        
    def get_img_url(self, obj):
        if obj.photo:
            return BASE_API_URL + obj.photo.url

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'
