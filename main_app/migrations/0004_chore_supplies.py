# Generated by Django 2.2.12 on 2023-01-02 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20230102_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='chore',
            name='supplies',
            field=models.ManyToManyField(to='main_app.Supply'),
        ),
    ]
