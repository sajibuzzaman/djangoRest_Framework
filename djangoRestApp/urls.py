from django.urls import path, include
from . import views
#router generic viewset
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('article', views.GenericArticleViewset, basename='article')


urlpatterns = [
    # Function Based Urls
    # path('',views.articlelist, name='articlelist'),
    # path('<int:pk>/',views.articledetails, name='articledetails'),

    # Class Based Urls
    path('', views.Articlelist.as_view(), name='articlelist'),
    path('<int:pk>/', views.Articledetails.as_view(), name='articledetails'),
    # path('generic/', views.GenericArticleView.as_view(), name='GenericArticleView'),
    # path('generic/<int:id>', views.GenericArticleView.as_view(), name='GenericArticleView'),
    path('viewset/', include(router.urls)),
]