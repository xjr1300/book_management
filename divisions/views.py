from typing import Optional

from django import forms
from django.urls import reverse, reverse_lazy
from django.views import generic

from core.mixins import FormActionMixin, PageTitleMixin

from .models import Division


class DivisionViewMixin:
    """部署ビューミックスイン"""

    model = Division


class DivisionSingleObjectMixin:
    """部署シングルオブジェクトミックスイン"""

    pk_url_kwarg = "code"


class DivisionFormMixin:
    """部署フォームミックスイン"""

    fields = ("code", "name")


class DivisionListView(DivisionViewMixin, PageTitleMixin, generic.ListView):
    """部署一覧クラスビュー"""

    title = "部署一覧"


class DivisionDetailView(
    DivisionViewMixin, DivisionSingleObjectMixin, PageTitleMixin, generic.DetailView
):
    """部署詳細クラスビュー"""

    title = "部署詳細"


class DivisionCreateView(
    DivisionViewMixin,
    DivisionSingleObjectMixin,
    DivisionFormMixin,
    PageTitleMixin,
    FormActionMixin,
    generic.CreateView,
):
    """部署登録クラスビュー"""

    title = "部署登録"
    action = "登録"

    def get_success_url(self) -> str:
        return reverse("divisions:division-detail", kwargs={"code": self.object.code})


class DivisionUpdateView(
    DivisionViewMixin,
    DivisionSingleObjectMixin,
    DivisionFormMixin,
    PageTitleMixin,
    FormActionMixin,
    generic.UpdateView,
):
    """部署更新クラスビュー"""

    title = "部署更新"
    action = "更新"

    def get_form(self, form_class: Optional[forms.Form] = None) -> forms.Form:
        form = super().get_form(form_class=form_class)
        form.fields["code"].widget.attrs["readonly"] = True
        return form

    def get_success_url(self) -> str:
        return reverse("divisions:division-detail", kwargs={"code": self.object.code})


class DivisionDeleteView(
    DivisionViewMixin, DivisionSingleObjectMixin, PageTitleMixin, generic.DeleteView
):
    """部署削除クラスビュー"""

    title = "部署削除"
    success_url = reverse_lazy("divisions:division-list")
