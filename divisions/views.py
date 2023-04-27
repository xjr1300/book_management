from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Division


def list(request: HttpRequest) -> HttpResponse:
    """部署一覧関数ビュー"""

    # すべての部署をデータベースから取得
    divisions = Division.objects.all()
    # コンテキストを作成
    context = {"division_list": divisions}
    # コンテキストでテンプレートをレンダリング
    return render(request, "divisions/division_list.html", context)
