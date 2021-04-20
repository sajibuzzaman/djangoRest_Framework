from django.urls import path
from . import views
urlpatterns = [
    path('articlelist/',views.articlelist, name='articlelist'),
    path('articledetails/<int:pk>/',views.articledetails, name='articledetails'),
]