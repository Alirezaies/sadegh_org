from django.urls import path
from .controllers.main_admin_panel_page import main_admin_panel_func
from admin.controllers.mail.mailbox import MailBoxView

urlpatterns = [
    path('', main_admin_panel_func, name='admin_dashboard'),

    # ============ Mail ============
    path('mail/', MailBoxView.as_view(), name='mailbox')
]