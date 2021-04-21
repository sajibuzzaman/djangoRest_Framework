from django.urls import path
from . import views
urlpatterns = [
    path('',views.articlelist, name='articlelist'),
    path('<int:pk>/',views.articledetails, name='articledetails'),
]