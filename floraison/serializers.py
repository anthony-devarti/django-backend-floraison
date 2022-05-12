from django.contrib.auth.models import User
from rest_framework import serializers
from floraison.models import item, Order, cookie_type, order_item
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

### IMPORTANT: May need to change gitpod link each time a new workspace is opened ###
# BASE_API_URL = 'https://warm-refuge-17443.herokuapp.com'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = '__all__'
    

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

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
            'id',
            'total',
            'paid',
            'completed',
            'due_date',
            'user',
            'order_item_set'
        ]
        depth = 2

class OrderItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    Order = OrderSerializer()
    class Meta:
        model = order_item
        fields = [
            'item',
            'Order',
            'unit_price',
            'message',
            'special_instructions',
        ]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token