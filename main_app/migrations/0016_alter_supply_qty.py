# Generated by Django 4.1.4 on 2023-01-04 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0015_merge_0007_supply_qty_0014_comment_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="supply",
            name="qty",
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]