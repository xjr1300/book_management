from typing import Any

from rest_framework import exceptions, serializers

from books.models import Classification, ClassificationDetail


class ClassificationSerializer(serializers.Serializer):
    """書籍分類シリアライザー"""

    # 書籍分類コード
    code = serializers.CharField(max_length=3)
    # 書籍分類名
    name = serializers.CharField(max_length=80)
    # 作成日時
    created_at = serializers.DateTimeField(read_only=True)
    # 更新日時
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data: Any) -> Classification:
        """
        validated_dataから書籍分類を作成して返却する。

        Args:
            validated_data: 書籍分類シリアライザーが検証したデータ。

        Returns:
            書籍分類モデルインスタンス。
        """
        return Classification.objects.create(**validated_data)

    def update(self, instance: Classification, validated_data: Any) -> Classification:
        """
        既存の書籍分類モデルインスタンスをvalidated_dataで更新して返却する。

        Args:
            instance: 更新する書籍分類モデルインスタンス。
            validated_data: 書籍分類シリアライザーが検証したデータ。

        Returns:
            書籍分類モデルインスタンス。
        """
        instance.code = validated_data.get("code", instance.code)
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class ClassificationDetailUpdateSerializer(serializers.ModelSerializer):
    """書籍分類詳細更新用シリアライザー"""

    # 書籍分類コード
    classification_code = serializers.CharField(
        max_length=3, source="classification", label="書籍分類コード"
    )

    class Meta:
        model = ClassificationDetail
        fields = [
            "classification_code",
            "name",
        ]

    def _get_classification(self, classification_code: str) -> Classification:
        """書籍分類コードから書籍分類モデルインスタンスを取得する。

        Args:
            classification_code: 書籍分類コード。
        Returns:
            書籍分類モデルインスタンス。
        Exceptions:
            rest_framework.exceptions.NotFound: 書籍分類が見つからない場合。
        """
        try:
            return Classification.objects.get(code=classification_code)
        except Classification.DoesNotExist:
            raise exceptions.NotFound(detail="Classification doesn't exist")

    def update(
        self, instance: ClassificationDetail, validated_data: Any
    ) -> ClassificationDetail:
        """書籍分類詳細を更新する。

        Args:
            validated_data: 書籍分類詳細シリアライザーが検証したデータ。
        Returns:
            更新した書籍分類詳細モデルインスタンス。
        Exceptions:
            rest_framework.exceptions.NotFound: 書籍分類が見つからない場合。
        """
        validated_data["classification"] = self._get_classification(
            validated_data["classification"]
        )
        return super().update(instance, validated_data)
