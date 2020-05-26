from django.urls import path
from .controllers.main_admin_panel_page import main_admin_panel_func

urlpatterns = [
    path('', main_admin_panel_func, name='admin_dashboard')
]