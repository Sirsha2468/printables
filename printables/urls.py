from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('products/', views.product, name="products"),
    path('product/<int:pk>', views.product_details, name="product"),
    path('products/stickers/', views.stickers, name="stickers"),
    path('products/posters/', views.posters, name="posters"),
    path('accounts/', include('accounts.urls'), name='accounts')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 