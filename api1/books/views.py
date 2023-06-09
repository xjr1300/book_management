from rest_framework import generics, permissions, serializers, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from books.models import Book, Classification, ClassificationDetail

from .serializers import (
    BookReadOnlySerializer,
    BookWriteOnlySerializer,
    ClassificationDetailSerializer,
    ClassificationDetailUpdateSerializer,
    ClassificationSerializer,
)


@api_view(["GET", "POST"])
def classification_list(request: Request) -> Response:
    """すべての書籍分類を返却するか、書籍分類を登録する。

    GETメソッドの場合は、すべての書籍分類モデルインスタンスを返却する。
    POSTメソッドの場合は、書籍分類モデルインスタンスを登録する。

    Args:
        request: リクエストインスタンス。
    Returns:
        レスポンス。
    """
    if request.method == "GET":
        # GETメソッドの場合は、すべての書籍分類モデルインスタンスを返却
        classifications = Classification.objects.all()
        serializer = ClassificationSerializer(classifications, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        # POSTメソッドの場合は、書籍分類モデルインスタンスを登録
        serializer = ClassificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def classification_detail(request: Request, code: str) -> Response:
    """
    書籍分類を取得、更新または削除する。

    Args:
        request: リクエストインスタンス。
        code: 書籍分類コード。
    Returns:
        レスポンス。
    """
    # 書籍分類コードから書籍分類モデルインスタンスを取得
    try:
        instance = Classification.objects.get(code=code)
    except Classification.DoesNotExist:
        # 書籍分類モデルインスタンスを取得できない場合は、`404 Not Found`を返却
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        # GETメソッドの場合は、書籍分類モデルインスタンスを返却
        serializer = ClassificationSerializer(instance)
        return Response(serializer.data)

    elif request.method == "PUT":
        # PUTメソッドの場合は、書籍分類モデルインスタンスを更新して返却
        # 書籍分類コードの更新は不可
        request.data["code"] = code
        serializer = ClassificationSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        # DELETEメソッドの場合は、書籍分類モデルインスタンスを削除
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClassificationDetailListCreateView(generics.ListCreateAPIView):
    """書籍分類詳細一覧登録ビュー"""

    queryset = ClassificationDetail.objects.all()
    serializer_class = ClassificationDetailSerializer


class ClassificationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """書籍分類詳細詳細更新削除ビュー"""

    queryset = ClassificationDetail.objects.all()
    serializer_class = ClassificationDetailSerializer
    lookup_field = "code"

    def get_serializer_class(self) -> serializers.Serializer:
        if self.request.method.lower() in ("put", "patch"):
            return ClassificationDetailUpdateSerializer
        return super().get_serializer_class()


class BookViewSet(viewsets.ModelViewSet):
    """書籍ビューセット"""

    queryset = Book.objects.all()
    serializer_class = BookReadOnlySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]

    def get_serializer_class(self) -> serializers.Serializer:
        """書籍シリアライザークラスを返却する。

        Returns:
            書籍シリアライザー。
        """
        if self.request.method.lower() in ("post", "put", "patch", "delete"):
            return BookWriteOnlySerializer
        return BookReadOnlySerializer
