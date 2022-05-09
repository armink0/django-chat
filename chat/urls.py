from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', include('chat_app.urls')),
    path('admin/', admin.site.urls),
]
