from django.urls import path
from . import views

app_name = "blogs-api"

urlpatterns = [
    path('list/', views.PostListAPIView.as_view(), name='list'),
    path('create/', views.PostCreateAPIView.as_view(), name='create'),
    path('detail/<id>/', views.PostRetrieveAPIView.as_view(), name='detail'),
    path('update/<id>/', views.PostUpdateAPIView.as_view(), name='update'),
    path('delete/<id>/', views.PostDestroyAPIView.as_view(), name='delete'),
]