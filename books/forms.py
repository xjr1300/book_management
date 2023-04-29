from django import forms

from .models import Book, Classification


class BookForm(forms.ModelForm):
    """書籍フォーム"""

    classification = forms.ModelChoiceField(
        label="書籍分類", queryset=Classification.objects.all(), empty_label=None
    )

    class Meta:
        model = Book
        fields = (
            "title",
            "classification",
            "classification_detail",
            "authors",
            "isbn",
            "publisher",
            "published_at",
            "division",
            "disposed",
            "disposed_at",
        )

    def __init__(self, *args, **kwargs) -> None:
        """イニシャライザ"""
        super().__init__(*args, **kwargs)
        self.fields["classification_detail"].empty_label = None
        self.fields["division"].empty_label = None
