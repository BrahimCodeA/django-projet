
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import login_user, user_logout, signup, contact
from store.views import cart , add_to_cart , delete_cart, product_detail, goodie_detail , add_to_cart_goodies, home, delete_orders, remove_from_cart, MHACategoryView, NarutoCategoryView, OnePieceCategoryView 


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', login_user, name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('cart/', cart, name='cart'),
    path('cart/delete', delete_cart, name='delete-cart'),
    path('cart/delete/order/<int:order_id>/', delete_orders, name='delete-order'),
    path('remove-from-cart/<int:order_id>/', remove_from_cart, name='remove-from-cart'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    
    path('product/<str:slug>/', product_detail, name='product'),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name='add-to-cart'),
    
    path('goodie/<slug:slug>/', goodie_detail, name='goodie'),
    path('goodie/<slug:slug>/add-to-cart/', add_to_cart_goodies, name='add-to-cart-goodies'),
    
    path('mha/', MHACategoryView.as_view(), name='mha_category'),
    path('naruto/', NarutoCategoryView.as_view(), name='naruto_category'),
    path('onepiece/', OnePieceCategoryView.as_view(), name='onepiece_category'),
    
    path('contact/', contact, name='contact'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)









