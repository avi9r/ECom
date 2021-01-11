from django.urls import include, path
from store import views
urlpatterns = [
    
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('account', views.account, name='account'),
    path('product-list', views.product_list, name='product-list'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('checkout', views.checkout, name='checkout'),
]