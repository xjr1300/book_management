from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.views import LogoutView as DjangoLogoutView

from core.mixins import PageTitleMixin


class LoginView(PageTitleMixin, DjangoLoginView):
    """ログインビュー"""

    title = "ログイン"
    template_name = "accounts/login.html"


class LogoutView(PageTitleMixin, DjangoLogoutView):
    """ログアウトビュー"""

    title = "ログアウト"
    template_name = "accounts/logout.html"
