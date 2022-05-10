from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('context_processor/', include('myapp_one.urls')),
    path('content_type/', include('myapp_two.urls')),
]
