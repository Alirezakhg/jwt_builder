from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'authjwt'

urlpatterns = [
    # http://127.0.0.1:8000/auth/token/
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # http://127.0.0.1:8000/auth/token/refresh/
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
