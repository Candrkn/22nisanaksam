# Generated by Django 4.2.14 on 2024-07-30 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_yorum'),
    ]

    operations = [
        migrations.AddField(
            model_name='yorum',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
