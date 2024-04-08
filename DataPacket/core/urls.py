from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import IOTDataViewSet

router = DefaultRouter()
router.register("data", IOTDataViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls))
]
