from django.contrib.auth.models import User
from rest_framework import serializers
from floraison.models import item, order, cookie_type, order_item

### IMPORTANT: May need to change gitpod link each time a new workspace is opened ###
BASE_API_URL = 'https://8000-anthonydeva-djangobacke-pk8s8czgzh1.ws-us43.gitpod.io/'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class ItemSerializer(serializers.ModelSerializer):
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

class CookieTypeSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_cookie_img_url')
    class Meta:
        model = cookie_type
        fields = "__all__"

    def get_cookie_img_url(self, obj):
        if obj.image:
            return BASE_API_URL + obj.image.url


##take the cart and do https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-multiple-objects kind of things to make a new order, it add all of the items in the cart to the order items table with the order id of the new order that has just been made
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_item
        fields=['message', 'item', 'order', 'unit_price', 'special_instructions']
    def create(self, validated_data):
        from pprint import pprint
        pprint(self)