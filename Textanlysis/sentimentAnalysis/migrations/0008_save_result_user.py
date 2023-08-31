# Generated by Django 4.1.5 on 2023-08-23 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sentimentAnalysis', '0007_remove_save_result_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='save_result',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
