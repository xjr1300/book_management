from django.db import models

from core.models import TimestampModel


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
