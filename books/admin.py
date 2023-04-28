from django.contrib import admin

from .models import Book, Classification, ClassificationDetail


class ClassificationAdmin(admin.ModelAdmin):
    """書籍分類モデルアドミン"""

    list_display = (
        "code",
        "name",
        "created_at",
        "updated_at",
    )


class ClassificationDetailAdmin(admin.ModelAdmin):
    """書籍分類詳細モデルアドミン"""

    list_display = (
        "code",
        "classification",
        "name",
        "created_at",
        "updated_at",
    )
    list_filter = ("classification",)


class BookAdmin(admin.ModelAdmin):
    """書籍モデルアドミン"""

    list_display = (
        "title",
        "classification_detail",
        "authors",
        "published_at",
        "division",
    )
    list_filter = (
        "classification_detail__classification",
        "division",
    )
    search_fields = (
        "title",
        "classification_detail__classification__name",
        "classification_detail__name",
        "authors",
        "division__name",
    )


admin.site.register(Classification, ClassificationAdmin)
admin.site.register(ClassificationDetail, ClassificationDetailAdmin)
admin.site.register(Book, BookAdmin)
