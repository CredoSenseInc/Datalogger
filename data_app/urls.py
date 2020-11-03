from .views import DataListView, DataCreateView, DataDetailView, DataUpdateView, DataDeleteView
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'datas', views.DataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('data-list/', DataListView.as_view(), name='data-list'),
    path('data-create/', DataCreateView.as_view(), name='data-create'),
    path('data-detail/<int:pk>', DataDetailView.as_view(),name='data-detail'),
    path('data-update/<int:pk>', DataUpdateView.as_view(),name='data-update'),
    path('data-delete/<int:pk>', DataDeleteView.as_view(),name='data-delete'),
]
