from django.urls import path

from .controllers.main_admin_panel_page import main_admin_panel_func
from admin.controllers.mail.mailbox import MailBoxView
from admin.controllers.mail.mail_view import MailView

urlpatterns = [
    path('', main_admin_panel_func, name='admin_dashboard'),

    # ============ Mail ============
    path('mail/', MailBoxView.as_view(), name='mailbox'),
    path('mail/view/<int:pk>/', MailView.as_view(), name='mail_view'),
]