
from django.contrib.auth.views import LogoutView
from django.urls import path

from AppAlonger.views import alonger
from accounts.views import loging_request, register_request

urlpatterns = [
    path('login/', loging_request, name="Login"),

    path('register/', register_request, name="Registro"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="Logout"),


]