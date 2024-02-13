from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet, TaskMemberViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'task-members', TaskMemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
