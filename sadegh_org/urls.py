from django.contrib import admin
from django.urls import path

from alirezaies.controllers import (
    home,
    hearts,
    nil
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.HomeView().home_controller, name='home'),
    path('hearts/', hearts.hearts_controller, name='hearts'),
    path('nil/', nil.nil_controller, name='nil')
]
