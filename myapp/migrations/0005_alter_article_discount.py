# Generated by Django 5.0.6 on 2024-07-09 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_article_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='discount',
            field=models.FloatField(default=20),
        ),
    ]
