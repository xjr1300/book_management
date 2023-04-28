from django.db import models


class TimestampModel(models.Model):
    """作成日時と更新日時をモデルフィールドに持つ抽象基本モデル"""

    # 作成日時
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    class Meta:
        abstract = True
