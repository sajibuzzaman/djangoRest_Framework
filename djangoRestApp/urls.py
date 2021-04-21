from django.urls import path
from . import views
urlpatterns = [
    # Function Based Urls
    # path('',views.articlelist, name='articlelist'),
    # path('<int:pk>/',views.articledetails, name='articledetails'),

    # Class Based Urls
    path('', views.Articlelist.as_view(), name='articlelist'),
    path('<int:pk>/', views.Articledetails.as_view(), name='articledetails'),
]