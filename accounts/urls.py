from django.urls import path

from accounts.views import CreateUserView, LoginView, logout_view


urlpatterns = [
    path('', LoginView.as_view(), name='login_url'),
    path('register/', CreateUserView.as_view(), name='register_url'),
    path('logout/', logout_view, name='logout_url'),

]