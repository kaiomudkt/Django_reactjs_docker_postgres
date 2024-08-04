from django.urls import path
from .views import *

urlpatterns = [
    #Authentication
    path('auth/login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/register/', RegisterView.as_view(), name='auth_register'),

    #Profile
    # path('profile/', getProfile, name='profile'),
    # path('profile/update/', updateProfile, name='update-profile'),

    # Authentication
    # path('auth/login/', login_view, name='login'),
    # path('auth/register/', register_view, name='user_register'),
    # path('auth/logout/', LogoutView, name='logout'),
    # path('auth/refresh-token/', RefreshTokenView, name='refresh_token'),

    # # User Management
    # path('user/', UserListView, name='user_list'),
    # path('user/<uuid:id>/', UserDetailView, name='user_detail'),
    # path('user/profile/', UserProfileView, name='user_profile'),  # Para obter/atualizar o perfil do usuário logado
    # path('user/<uuid:id>/profile/', UserProfileDetailView, name='user_profile_detail'),  # Para perfis de outros usuários

    # # Password Management
    # path('user/reset-password/', ResetPasswordView, name='reset_password'),
    # path('user/reset-password/confirm/', ResetPasswordConfirmView, name='reset_password_confirm'),
    # path('user/change-password/', ChangePasswordView, name='change_password'),

    # # Account Verification
    # path('user/verify-email/', VerifyEmailView, name='verify_email'),
    # path('user/verify-email/confirm/', VerifyEmailConfirmView, name='verify_email_confirm'),
]
