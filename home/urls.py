#!/usr/bin/python
from django.urls import path
from django.urls import re_path
from django.contrib.auth import views as auth_views
from home.views import index
from home.views import connection_views
from home.views import registration
from home.views import agences
from home.views import contact

urlpatterns = [
    re_path(r'^$', index.IndexView.as_view(), name='index'),
    re_path(r'^index.php$', index.IndexView.as_view(), name='index'),
    re_path(r'^setDevice.php$', index.DeviseView.as_view(), name='set_devise'),
    re_path(r'^login.php$', connection_views.login_view.as_view(), name='login'),
    re_path(r'^forgetpassword.php$', connection_views.ForgetPassword.as_view(), name='sendPassword'),
    re_path(r'^mailNotConfirmed.php$', connection_views.MailNotConfirmedView.as_view(), name='mail_not_confirmed'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', connection_views.ResetDoneView.as_view(), name='password_reset_complete'),
    path('reset/done/', connection_views.ResetDoneView.as_view(), name='password_change_done'),
    path('changepassword.php', connection_views.ChangePasswordView.as_view(),name='password_change'),
    path('logout.php', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^registration.php$', registration.RegisterationView.as_view(), name='registration'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
        registration.activate, name='activate'),
    path('contact.php', contact.ContactView.as_view(),name='contact'),
    re_path(r'^agences.php$', agences.AgencesView.as_view(), name='agences'),
    re_path(r'^agences/register$', agences.RegisterView.as_view(), name='agences_register'),
    re_path(r'^agences/manage$', agences.ManageAgenceView.as_view(), name='manage_agence'),
]
