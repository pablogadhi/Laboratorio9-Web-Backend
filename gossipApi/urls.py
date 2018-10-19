from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from gossips import views

router = routers.DefaultRouter()
router.register(r'gossips', views.GossipViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]