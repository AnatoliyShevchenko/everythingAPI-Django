from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from rest_framework.routers import DefaultRouter

from lessons.views import BookView
from auths.views import UserView, UserRegView, LoginView, LogoutView
from banks.views import CardView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
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
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
urlpatterns += [
    path('api/v1/', include(router.urls))
]