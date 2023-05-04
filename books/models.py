import ulid
from django.db import models

from core.models import TimestampModel, ULIDField


class Classification(TimestampModel):
    """書籍分類モデル"""

    # 書籍分類コード
    code = models.CharField("書籍分類コード", primary_key=True, max_length=3)
    # 書籍分類名
    name = models.CharField("書籍分類名", max_length=80)

    class Meta:
        db_table = "classifications"
        verbose_name = verbose_name_plural = "書籍分類"
        ordering = ("code",)

    def __str__(self) -> str:
        """書籍分類モデルインスタンス名を返却する。

        Returns:
            書籍分類モデルインスタンス名。
        """
        return self.name

    def full_name(self) -> str:
        """書籍分類モデルインスタンスのフルネームを返却する。

        Returns:
            書籍分類モデルのフルネーム。
        """
        return f"{self.code}: {self.name}"


class ClassificationDetail(TimestampModel):
    """書籍分類詳細モデル"""

    # 書籍分類詳細コード
    code = models.CharField("書籍分類詳細コード", primary_key=True, max_length=3)
    # 書籍分類
    classification = models.ForeignKey(
        Classification,
        db_column="classification_code",
        on_delete=models.PROTECT,
        related_name="classification_details",
        verbose_name="書籍分類詳細",
    )
    # 書籍分類詳細名
    name = models.CharField("書籍分類詳細名", max_length=80)

    class Meta:
        db_table = "classification_details"
        verbose_name = verbose_name_plural = "書籍分類詳細"
        ordering = ("code",)

    def __str__(self) -> str:
        """書籍分類詳細モデルインスタンス名を返却する。

        Returns:
            書籍分類詳細モデルインスタンス名。
        """
        return self.name

    def full_name(self) -> str:
        """書籍分類詳細モデルインスタンスのフルネームを返却する。

        Returns:
            書籍分類詳細モデルのフルネーム。
        """
        return f"{self.code}: {self.name}"


class Book(TimestampModel):
    """書籍モデル"""

    # 書籍ID
    id = ULIDField("書籍ID", primary_key=True, editable=False, default=ulid.ULID)
    # タイトル
    title = models.CharField("タイトル", max_length=120)
    # 書籍分類詳細
    classification_detail = models.ForeignKey(
        ClassificationDetail,
        db_column="classification_detail_code",
        on_delete=models.PROTECT,
        related_name="classification_detail_books",
        verbose_name="書籍分類詳細",
    )
    # 著者または訳者
    authors = models.TextField("著者または訳者", null=True, blank=True)
    # ISBN
    isbn = models.CharField("ISBN", max_length=40, null=True, blank=True)
    # 出版社
    publisher = models.CharField("出版社", max_length=80, null=True, blank=True)
    # 発行日
    published_at = models.DateField("発行日", null=True, blank=True)
    # 管理部署コード
    division = models.ForeignKey(
        "divisions.Division",
        db_column="division_code",
        on_delete=models.PROTECT,
        related_name="books",
        verbose_name="管理部署",
    )
    # 廃棄済み
    disposed = models.BooleanField("廃棄済み", default=False)
    # 廃棄日
    disposed_at = models.DateField("廃棄日", null=True, blank=True)

    class Meta:
        db_table = "books"
        verbose_name = verbose_name_plural = "書籍"
        ordering = ("id",)

    def __str__(self) -> str:
        """書籍のタイトルを返却する。

        Returns:
            書籍のタイトル。
        """
        return self.title
