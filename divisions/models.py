# django.db.modelsモジュールをインポート
from django.db import models


class Division(models.Model):
    """部署モデル

    django.db.models.Modelを継承したDivisionモデルを定義します。
    """

    # 部署コード
    code = models.CharField("部署コード", primary_key=True, max_length=2)
    # 部署名
    name = models.CharField("部署名", max_length=80)
    # 作成日時
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    class Meta:
        db_table = "divisions"
        verbose_name = verbose_name_plural = "部署"
        ordering = ("code",)

    def __str__(self) -> str:
        """部署モデルインスタンス名を返却する。

        Returns:
            部署モデルインスタンス名。
        """
        return self.name

    def full_name(self) -> str:
        """部署モデルインスタンスのフルネームを返却する。

        Returns:
            部署モデルインスタンスのフルネーム。
        """
        return f"{self.code}: {self.name}"

    def name_len(self) -> int:
        """部署名の文字数を返却する。

        Returns:
            部署名の文字数。
        """
        return len(self.name)
