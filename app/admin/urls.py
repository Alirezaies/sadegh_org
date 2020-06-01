from django.urls import path

from admin.controllers.mail.mailbox import MailBoxView
from admin.controllers.mail.mail_view import MailView
from admin.controllers.mail.delete_mail import DeleteMail
from admin.controllers.users.users_list_view import UsersList
from admin.controllers.users.user_edit import EditUser
from admin.controllers.users.delete_user import DeleteUser
from admin.controllers.users.user_profile import UserProfileView
from admin.controllers.users.create_user import CreateUserView
from admin.controllers.cv.bio import BioView

from .controllers.main_admin_panel_page import main_admin_panel_func


urlpatterns = [
    path('', main_admin_panel_func, name='admin_dashboard'),

    # ============ Mail ============
    path('mail/', MailBoxView.as_view(), name='mailbox'),
    path('mail/view/<int:pk>/', MailView.as_view(), name='mail_view'),
    path('mail/delete/<int:pk>/', DeleteMail.as_view(), name='delete_mail'),

    # ============ Users ============
    path('users/', UsersList.as_view(), name='users_list'),
    path('users/edit/<int:pk>/', EditUser.as_view(), name='user_edit'),
    path('users/delete/<int:pk>/', DeleteUser.as_view(), name='user_delete'),
    path('users/view/<str:username>', UserProfileView.as_view(), name='user_profile_view'),
    path('users/create/', CreateUserView.as_view(), name='user_create'),

    # ============= CV ============
    path('cv/bio/', BioView.as_view(), name='cv_bio'),

]
