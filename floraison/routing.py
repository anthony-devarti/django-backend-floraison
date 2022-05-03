from rest_framework.routers import DefaultRouter
from .views import OrderItemViewSet, CustomerOrderViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

router = DefaultRouter()

router.register(order_items, OrderItemsViewset)
router.register(orders, CustomerOrderViewSet)

class NestedDefaultRouter(NestedViewSetMixin, DefaultRouter):
    pass

router = NestedDefaultRouter()

order_items_router = router.register('order_items', OrderItemViewSet)
order_items_router(
    'order',
    CustomerOrderViewSet,
    base_name='order_items-order',
##I am now at the bottom of https://medium.com/@EnterGodMode__/simple-nested-api-using-django-rest-framework-d2dd9f0ff093
# unsure of what this is supposed to be doing, but it doesn't seem to have made any changes to endpoints    

)