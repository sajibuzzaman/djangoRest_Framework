from django.urls import path, include
from rest_framework.routers import DefaultRouter
from djangoRestApp.viewsets import ArticleViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('article', ArticleViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]