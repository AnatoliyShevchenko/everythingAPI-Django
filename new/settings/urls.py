from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from rest_framework.routers import DefaultRouter

from lessons.views import BookView
from auths.views import (
    UserView, 
    UserRegView, 
    LoginView, 
    LogoutView, 
)
from banks.views import (
    CardView, 
    TerminalView, 
    CardToCardView, 
    CardToTerminalView,
    TransactionView,
)
from asyncs.views import AsyncViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path(
        'api/token/', 
        TokenObtainPairView.as_view(), 
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/', 
        TokenRefreshView.as_view(), 
        name='token_refresh'
    ),
    path(
        'api/token/verify/', 
        TokenVerifyView.as_view(), 
        name='token_verify'
    ),
]

router: DefaultRouter = DefaultRouter(
    trailing_slash=True
)

router.register('books', BookView)
router.register('users', UserView)
router.register('cards', CardView)
router.register('reg_user', UserRegView)
router.register('login', LoginView)
router.register('logout', LogoutView)
router.register('terminals', TerminalView)
router.register('async', AsyncViewSet)
router.register('card-to-card', CardToCardView)
router.register('card-to-terminal', CardToTerminalView)
router.register('transactions', TransactionView)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
urlpatterns += [
    path('api/v1/', include(router.urls))
]