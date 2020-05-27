from django.urls import (
    path,
    re_path,
    include,
)
from django.contrib.auth import views as auth_views

from authentication.views import signup
from alirezaies.controllers import (
    home,
    hearts,
    nil,
)

urlpatterns = [

    # ============ Admin Panel ============
    path('admin/', include('admin.urls')),

    # ============ Home ============
    path('', home.HomeView().home_controller, name='home'),

    # ============ Hearts ============
    path('hearts/', hearts.hearts_controller, name='hearts'),
    path('nil/', nil.nil_controller, name='nil'),

    # ============ Auth ============
    path('signup/', signup.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # ============ Forget Password ============
    path(
        'reset/',
        auth_views.PasswordResetView.as_view(
            template_name='auth/password_reset/password_reset.html',
            email_template_name='auth/password_reset/password_reset_email.html',
            subject_template_name='auth/password_reset/passwod_reset_subject.txt',
        ),
        name='password_reset'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='auth/password_reset/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    re_path(
        '^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='auth/password_reset/password_reset_confirm.html',
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='auth/password_reset/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),

    # ============ Change Password ============
    path(
        'settings/change_password/',
        auth_views.PasswordChangeView.as_view(
            template_name='auth/password_reset/change_password.html'
        ),
        name='change_password'
    ),
    path(
        'settings/password_change_done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='auth/password_reset/change_password_done.html'
        ),
        name='password_change_done'
    ),
]

handler404 = 'alirezaies.controllers.error_handler.error_404'
handler403 = 'alirezaies.controllers.error_handler.error_403'
handler500 = 'alirezaies.controllers.error_handler.error_500'
