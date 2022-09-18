from django.urls import path

from .views import(
    home_page, item_page, success_page, cancelled_page,
    stripe_config, create_checkout_session, add_to_cart,
    del_from_cart
)

urlpatterns = [
    path('', home_page, name='home'),
    path('item/<int:id>', item_page, name='item'),
    path('config/', stripe_config, name='strip_config'),
    path('buy/<int:id>', create_checkout_session, name='checkout_session'),
    path('add_to_cart/<int:id>', add_to_cart, name='add_to_cart'),
    path('del_from_cart/<int:id>', del_from_cart, name='del_from_cart'),
    path('success/', success_page, name='success'),
    path('cancelled/', cancelled_page, name='cancelled'),
]