from typing import Any, Dict, Type

from django import forms
from django.db import transaction
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from .models import Division


class DivisionListView(generic.ListView):
    """部署一覧クラスビュー"""

    model = Division

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = "部署一覧"
        return ctx


class DivisionDetailView(generic.DetailView):
    """部署詳細クラスビュー"""

    model = Division
    pk_url_kwarg = "code"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = "部署詳細"
        return ctx


class DivisionCreateView(generic.CreateView):
    """部署登録クラスビュー"""

    model = Division
    pk_url_kwarg = "code"
    fields = ("code", "name")

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = "部署登録"
        ctx["action"] = "登録"
        return ctx

    def get_success_url(self) -> str:
        return reverse("divisions:division-detail", kwargs={"code": self.object.code})


class DivisionUpdateView(generic.UpdateView):
    """部署更新クラスビュー"""

    model = Division
    pk_url_kwarg = "code"
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


def delete(request: HttpRequest, code: str) -> HttpResponse:
    """部署削除関数ビュー

    Args:
        code: 部署コード
    """

    # 部署コードから部署モデルインスタンスを取得
    division = get_object_or_404(Division, pk=code)
    if request.method == "POST":
        with transaction.atomic():
            division.delete()
        return redirect("divisions:division-list")
    return render(
        request, "divisions/division_confirm_delete.html", {"division": division}
    )
