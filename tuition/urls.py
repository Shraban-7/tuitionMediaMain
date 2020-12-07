from django.urls import path
from .views import TuitionPostCreateView, TuitionListView, TuitionDetailView, load_cities

urlpatterns = [
    path('create/', TuitionPostCreateView.as_view(), name='create'),
    path('list/', TuitionListView.as_view(), name='list'),
    path('detail/<int:pk>/', TuitionDetailView.as_view(), name='detail'),
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
]
