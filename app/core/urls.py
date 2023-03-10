"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from products.api.viewsets import ProductViewset
from costumers.api.viewsets import CostumerViewset, PurchaseViewset



router = DefaultRouter()
router.register('products', ProductViewset)
router.register('costumers', CostumerViewset)
router.register('purchases', PurchaseViewset, basename="Purchase")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path(
        'api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
