from django.urls import path
from .views import to_do_list

urlpatterns = [
    path('', to_do_list, name='to_do'),
]