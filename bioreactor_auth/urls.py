from django.urls import path

from .views import LoginView, LogoutView,GetDeviceAuthenticationTokenView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('get-device-token/', GetDeviceAuthenticationTokenView.as_view()),
]