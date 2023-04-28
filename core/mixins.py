from typing import Any, Dict

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
