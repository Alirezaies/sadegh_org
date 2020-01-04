from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from authentication.views import signup
from alirezaies.controllers import (
    home,
    hearts,
    nil,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.HomeView().home_controller, name='home'),

    # ============ Hearts ============
    path('hearts/', hearts.hearts_controller, name='hearts'),
    path('nil/', nil.nil_controller, name='nil'),

    # ============ Auth ============
    path('signup/', signup.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
