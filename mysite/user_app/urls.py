from django.urls import path
from . import views 
from .views import UserEditView, PasswordsChangeView, password_success# 
urlpatterns = [
    path('register/',views.createUser,name="register"),
    path('verify/',views.verifyUser,name="verify"),
    path('login/',views.login_function,name="login"),
    path('success/',views.success,name="success"),
    path('logout/',views.logout_function,name='logout'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='accounts/change_password.html'), name='change-password'),
    path('password_success/', password_success, name='password_success'),
]
