from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('product/', include('product.urls')),
    path('order-management/', include('order_management.urls')),

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
