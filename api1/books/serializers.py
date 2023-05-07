from typing import Any

from rest_framework import exceptions, serializers

from books.models import Book, Classification, ClassificationDetail
from divisions.models import Division


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
    """更新用の書籍分類詳細更新用シリアライザー"""

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


class ClassificationDetailSerializer(ClassificationDetailUpdateSerializer):
    """一覧、詳細、登録及び削除用の書籍分類詳細シリアライザー"""

    # 書籍分類名
    classification_name = serializers.SerializerMethodField(
        "_get_classification_name", label="書籍分類名"
    )
    # 作成日時
    created_at = serializers.DateTimeField(read_only=True)
    # 更新日時
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = ClassificationDetail
        fields = [
            "code",
            "classification_code",
            "classification_name",
            "name",
            "created_at",
            "updated_at",
        ]

    def _get_classification_name(self, obj: ClassificationDetail) -> str:
        """書籍分類名を返却する。

        Args:
            obj: 書籍分類詳細モデルインスタンス。
        Returns:
            書籍分類名。
        """
        return obj.classification.name

    def create(self, validated_data: Any) -> ClassificationDetail:
        """書籍分類詳細を登録する。

        Args:
            validated_data: 書籍分類詳細シリアライザーが検証したデータ。
        Returns:
            作成した書籍分類詳細モデルインスタンス。
        Exceptions:
            rest_framework.exceptions.NotFound: 書籍分類が見つからない場合。
        """
        validated_data["classification"] = self._get_classification(
            validated_data["classification"]
        )
        return super().create(validated_data)


class ClassificationReadOnlySerializer(serializers.ModelSerializer):
    """書籍分類モデル読み込み専用シリアライザー"""

    class Meta:
        model = Classification
        fields = (
            "code",
            "name",
        )


class ClassificationDetailReadOnlySerializer(serializers.ModelSerializer):
    """書籍分類詳細モデル読み込み専用シリアライザー"""

    classification = ClassificationReadOnlySerializer(label="書籍分類")

    class Meta:
        model = Classification
        fields = (
            "code",
            "classification",
            "name",
        )


class DivisionReadOnlySerializer(serializers.ModelSerializer):
    """部署読み込み専用モデルシリアライザー"""

    class Meta:
        model = Division
        fields = (
            "code",
            "name",
        )


class BookReadOnlySerializer(serializers.ModelSerializer):
    """書籍読み込み専用シリアライザー"""

    # 書籍ID
    id = serializers.CharField(label="書籍ID")
    # 書籍分類詳細
    classification_detail = ClassificationDetailReadOnlySerializer(label="書籍分類詳細")
    # 管理部署
    division = DivisionReadOnlySerializer(label="管理部署")

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "classification_detail",
            "authors",
            "isbn",
            "publisher",
            "published_at",
            "division",
            "disposed",
            "disposed_at",
            "created_at",
            "updated_at",
        )


class BookWriteOnlySerializer(serializers.ModelSerializer):
    """書籍書き込み専用シリアライザー"""

    # 書籍ID
    id = serializers.CharField(max_length=26, read_only=True)
    # 書籍分類詳細コード
    classification_detail_code = serializers.CharField(
        max_length=3, source="classification_detail", label="書籍分類詳細コード"
    )
    # 管理部署コード
    division_code = serializers.CharField(
        max_length=2, source="division", label="管理部署コード"
    )

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "classification_detail_code",
            "authors",
            "isbn",
            "publisher",
            "published_at",
            "division_code",
            "disposed",
            "disposed_at",
        )

    def _get_classification_detail(self, code: str) -> ClassificationDetail:
        """書籍分類詳細コードから書籍分類詳細モデルインスタンスを取得して返却する。

        Args:
            code: 書籍分類詳細コード。
        Returns:
            書籍分類詳細モデルインスタンス。
        Exceptions:
            rest_framework.exceptions.NotFound: 書籍分類詳細が見つからない場合。
        """
        try:
            return ClassificationDetail.objects.get(code=code)
        except ClassificationDetail.DoesNotExist:
            raise exceptions.NotFound(detail="Classification detail doesn't exist")

    def _get_division(self, code: str) -> Division:
        """部署コードから部署モデルインスタンスを取得して返却する。

        Args:
            code: 部署コード。
        Returns:
            部署モデルインスタンス。
        Exceptions:
            rest_framework.exceptions.NotFound: 部署が見つからない場合。
        """
        try:
            return Division.objects.get(code=code)
        except Division.DoesNotExist:
            raise exceptions.NotFound(detail="Division doesn't exist")

    def _organize_validated_data(self, validated_data: Any) -> Any:
        """書籍書き込みシリアライザーが検証したデータを整理する。

        書籍書き込みシリアライザーが検証したデータに、書籍分類詳細及び部署モデルインスタンスを設定する。

        Args:
            validated_data: 書籍書き込みシリアライザーが検証したデータ。
        Returns:
            書籍書き込みシリアライザーが検証したデータを整理した結果。
        Exceptions:
            rest_framework.exceptions.NotFound: 書籍分類詳細または部署が見つからない場合。
        """
        validated_data["classification_detail"] = self._get_classification_detail(
            validated_data["classification_detail"]
        )
        validated_data["division"] = self._get_division(validated_data["division"])
        return validated_data

    def create(self, validated_data: Any) -> Book:
        """書籍を登録する。

        Args:
            validated_data: 書籍書き込み専用シリアライザーが検証したデータ。
        Returns:
            作成した書籍モデルインスタンス。
        Exceptions:
            rest_framework.exceptions.NotFound: 書籍分類詳細または部署が見つからない場合。
        """
        return super().create(self._organize_validated_data(validated_data))

    def update(self, instance: Any, validated_data: Any) -> Book:
        """書籍を更新する。

        Args:
            validated_data: 書籍書き込み専用シリアライザーが検証したデータ。
        Returns:
            更新した書籍モデルインスタンス。
        Exceptions:
            rest_framework.exceptions.NotFound: 書籍分類詳細または部署が見つからない場合。
        """
        return super().update(instance, self._organize_validated_data(validated_data))
