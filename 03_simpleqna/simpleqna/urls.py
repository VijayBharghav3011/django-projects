from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('user_authenticate.urls')),
    path('',include('qna.urls')),
]
