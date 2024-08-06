from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authetication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authetication/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
