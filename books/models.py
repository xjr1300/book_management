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
