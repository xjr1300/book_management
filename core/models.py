from django.db import models


class TimestampModel(models.Model):
    """作成日時と更新日時をモデルフィールドに持つ抽象基本モデル"""

    # 作成日時
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    class Meta:
        abstract = True


class ULIDField(models.CharField):
    """ULIDモデルフィールド"""

    def __init__(self, *args, **kwargs) -> None:
        kwargs["max_length"] = 26
        super().__init__(*args, **kwargs)

    def db_type(self, connection) -> str:
        return "char(26)"
