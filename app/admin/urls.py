from django.urls import path

from admin.controllers.mail.mailbox import MailBoxView
from admin.controllers.mail.mail_view import MailView
from admin.controllers.mail.delete_mail import DeleteMail
from admin.controllers.users.users_list_view import UsersList

from .controllers.main_admin_panel_page import main_admin_panel_func


urlpatterns = [
    path('', main_admin_panel_func, name='admin_dashboard'),

    # ============ Mail ============
    path('mail/', MailBoxView.as_view(), name='mailbox'),
    path('mail/view/<int:pk>/', MailView.as_view(), name='mail_view'),
    path('mail/delete/<int:pk>/', DeleteMail.as_view(), name='delete_mail'),

    # ============ Users ============
    path('users/', UsersList.as_view(), name='users_list'),
]
