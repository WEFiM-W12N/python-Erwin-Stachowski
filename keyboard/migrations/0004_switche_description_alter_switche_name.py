# Generated by Django 4.0.3 on 2022-05-06 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keyboard', '0003_switche_delete_switches'),
    ]

    operations = [
        migrations.AddField(
            model_name='switche',
            name='description',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='switche',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
