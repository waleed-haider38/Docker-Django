from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from core.views import ProjectViewSet, TaskViewSet
from products.views import ProductViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r"products", ProductViewSet, basename="product")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path("api/", include(router.urls)),
]