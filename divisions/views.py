from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Division


def list(request: HttpRequest) -> HttpResponse:
    """部署一覧関数ビュー"""

    # すべての部署をデータベースから取得
    divisions = Division.objects.all()
    # コンテキストを作成
    context = {"division_list": divisions}
    # コンテキストでテンプレートをレンダリング
    return render(request, "divisions/division_list.html", context)


def detail(request: HttpResponse, code: str) -> HttpResponse:
    """部署詳細ビュー

    Args:
        code: 部署コード
    """

    # 部署コードから部署モデルインスタンスを取得
    division = get_object_or_404(Division, pk=code)
    # コンテキストを渡してテンプレートをレンダリング
    return render(request, "divisions/division_detail.html", {"division": division})
