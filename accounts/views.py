from django.contrib.auth.views import LoginView as DjangoLoginView

from core.mixins import PageTitleMixin


class LoginView(PageTitleMixin, DjangoLoginView):
    """ログインビュー"""

    title = "ログイン"
    template_name = "accounts/login.html"
