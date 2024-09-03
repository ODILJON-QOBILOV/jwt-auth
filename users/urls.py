from django.urls import path
from .views import SignupApiView, AnotherPage, CustomTokenRefreshView, LoginApiView

urlpatterns = [
    path('api/register/', SignupApiView.as_view()),
    path('api/', AnotherPage.as_view()),
    path('api/token/refresh/', CustomTokenRefreshView.as_view()),
    path('api/login/', LoginApiView.as_view()),
    # other paths...
]
