from typing import Any

from rest_framework import serializers

from books.models import Classification


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
