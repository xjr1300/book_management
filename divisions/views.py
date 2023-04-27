from typing import Any, Dict, Type

from django import forms
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Division


class DivisionViewMixin:
    """部署ビューミックスイン"""

    model = Division


class DivisionSingleObjectMixin:
    """部署シングルオブジェクトミックスイン"""

    pk_url_kwarg = "code"


class DivisionListView(DivisionViewMixin, generic.ListView):
    """部署一覧クラスビュー"""

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = "部署一覧"
        return ctx


class DivisionDetailView(
    DivisionViewMixin, DivisionSingleObjectMixin, generic.DetailView
):
    """部署詳細クラスビュー"""

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = "部署詳細"
        return ctx


class DivisionCreateView(
    DivisionViewMixin, DivisionSingleObjectMixin, generic.CreateView
):
    """部署登録クラスビュー"""

    fields = ("code", "name")

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = "部署登録"
        ctx["action"] = "登録"
        return ctx

    def get_success_url(self) -> str:
        return reverse("divisions:division-detail", kwargs={"code": self.object.code})


class DivisionUpdateView(
    DivisionViewMixin, DivisionSingleObjectMixin, generic.UpdateView
):
    """部署更新クラスビュー"""

    fields = ("code", "name")

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = "部署更新"
        ctx["action"] = "更新"
        return ctx

    def get_form(self, form_class: Type[forms.Form] | None = None) -> forms.Form:
        form = super().get_form(form_class=form_class)
        form.fields["code"].widget.attrs["readonly"] = True
        return form

    def get_success_url(self) -> str:
        return reverse("divisions:division-detail", kwargs={"code": self.object.code})


class DivisionDeleteView(
    DivisionViewMixin, DivisionSingleObjectMixin, generic.DeleteView
):
    """部署削除クラスビュー"""

    success_url = reverse_lazy("divisions:division-list")

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = "部署削除"
        return ctx
