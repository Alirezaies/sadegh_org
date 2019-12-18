from django.contrib import admin
from django.urls import path

from alirezaies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('hearts/', views.hearts, name='hearts'),
    path('nil/', views.nil, name='nil')
]
