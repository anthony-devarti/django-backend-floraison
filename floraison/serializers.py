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

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = order
#         fields = '__all__'

class CookieTypeSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_cookie_img_url')
    class Meta:
        model = cookie_type
        fields = "__all__"

    def get_cookie_img_url(self, obj):
        if obj.image:
            return BASE_API_URL + obj.image.url

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_item
        fields = [
            'message',
            'special_instructions',
        ]

class OrderSerializer(serializers.ModelSerializer, serializers.Serializer):
    order_items = serializers.ListField()

    class Meta:
        model = order
        fields = [
            'total',
            'paid',
            'completed',
            'due_date',
            'user',
            'order_items'
        ]

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = order.objects.create(**validated_data)
        for oi in order_items_data:
            item_id = oi.pop('item_id')
            item = item.objects.get(pk=item_id)
            oi.objects.create(order=order, item=item, **order_item)
        return order
