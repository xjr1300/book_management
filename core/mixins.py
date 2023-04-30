from typing import Any, Dict

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin as DjangoLoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.views import generic


class PageTitleMixin(generic.base.ContextMixin):
    """ページタイトルミックスイン"""

    title = None

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = self.title
        return ctx


class FormActionMixin(generic.base.ContextMixin):
    """フォームアクションミックスイン"""

    action = None

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["action"] = self.action
        return ctx


class LoginRequiredMixin(DjangoLoginRequiredMixin):
    """ログイン要求ミックスイン

    Djangoが提供するLoginRequiredMixinを拡張して、ログインしていないユーザーがページにアクセスする
    権限がないことを示すメッセージを、Djangoが適用するセッションフレームワークで通知できるようにします。
    このミックスインを継承するビューは、permission_denied_messageをオーバーライドすることで、ビューに
    あわせたメッセージを通知できます。
    """

    permission_denied_message = "ページにアクセスする権限がありません。"

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if not request.user.is_authenticated:
            messages.add_message(
                request, messages.WARNING, self.permission_denied_message
            )
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
