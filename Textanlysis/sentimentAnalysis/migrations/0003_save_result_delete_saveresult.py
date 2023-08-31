# Generated by Django 4.1.5 on 2023-08-21 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentimentAnalysis', '0002_saveresult_delete_inputtext'),
    ]

    operations = [
        migrations.CreateModel(
            name='save_result',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=1000)),
                ('sentiment', models.CharField(max_length=20)),
                ('confidence', models.FloatField(verbose_name='confidence')),
            ],
        ),
        migrations.DeleteModel(
            name='saveResult',
        ),
    ]