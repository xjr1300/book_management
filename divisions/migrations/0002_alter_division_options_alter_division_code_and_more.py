# Generated by Django 4.2 on 2023-04-27 08:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("divisions", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="division",
            options={
                "ordering": ("code",),
                "verbose_name": "部署",
                "verbose_name_plural": "部署",
            },
        ),
        migrations.AlterField(
            model_name="division",
            name="code",
            field=models.CharField(
                max_length=2, primary_key=True, serialize=False, verbose_name="部署コード"
            ),
        ),
        migrations.AlterField(
            model_name="division",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="作成日時"),
        ),
        migrations.AlterField(
            model_name="division",
            name="name",
            field=models.CharField(max_length=80, verbose_name="部署名"),
        ),
        migrations.AlterField(
            model_name="division",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="更新日時"),
        ),
        migrations.AlterModelTable(
            name="division",
            table="divisions",
        ),
    ]
