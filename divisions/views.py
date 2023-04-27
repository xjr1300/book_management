from django.db import transaction
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DivisionForm
from .models import Division


def list(request: HttpRequest) -> HttpResponse:
    """部署一覧関数ビュー"""

    # すべての部署をデータベースから取得
    divisions = Division.objects.all()
    # コンテキストを作成
    context = {
        "title": "部署一覧",
        "division_list": divisions,
    }
    # コンテキストでテンプレートをレンダリング
    return render(request, "divisions/division_list.html", context)


def detail(request: HttpResponse, code: str) -> HttpResponse:
    """部署詳細関数ビュー

    Args:
        code: 部署コード
    """

    # 部署コードから部署モデルインスタンスを取得
    division = get_object_or_404(Division, pk=code)
    # コンテキストを渡してテンプレートをレンダリング
    return render(
        request,
        "divisions/division_detail.html",
        {"title": "部署詳細", "division": division},
    )


def create(request: HttpResponse) -> HttpResponse:
    """部署登録関数ビュー"""

    if request.method == "POST":
        # POSTパラメーターから部署フォームを構築
        form = DivisionForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                division = form.save()
            return redirect("divisions:division-detail", code=division.code)
    else:  # request.method is "GET", maybe.
        # フォームを構築
        form = DivisionForm()
    # コンテキストを渡してテンプレートをレンダリング
    return render(
        request,
        "divisions/division_form.html",
        {"title": "部署登録", "form": form, "action": "登録"},
    )


def update(request: HttpRequest, code: str) -> HttpResponse:
    """部署更新関数ビュー

    Args:
        code: 部署コード
    """

    # 部署コードから部署モデルインスタンスを取得
    division = get_object_or_404(Division, pk=code)
    if request.method == "POST":
        # POSTパラメーターから部署フォームを構築
        form = DivisionForm(request.POST, instance=division)
        if form.is_valid():
            division = form.save(commit=False)
            division.code = code
            with transaction.atomic():
                division.save()
            return redirect("divisions:division-detail", code=division.code)
    else:  # request.method is "GET", maybe.
        # 部署モデルインスタンスから部署フォームを構築
        form = DivisionForm(instance=division)
    form.fields["code"].widget.attrs["readonly"] = True
    return render(
        request,
        "divisions/division_form.html",
        {"title": "部署更新", "form": form, "action": "更新"},
    )


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
