# Generated by Django 4.1.5 on 2023-08-23 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sentimentAnalysis', '0014_remove_save_result_id_save_result_s_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='save_result',
            name='s_no',
        ),
    ]
