# Generated by Django 4.0.3 on 2022-05-12 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('keyboard', '0006_switche_keycap'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='switche',
            name='description',
        ),
        migrations.RemoveField(
            model_name='switche',
            name='keycap',
        ),
        migrations.RemoveField(
            model_name='switche',
            name='model',
        ),
        migrations.AddField(
            model_name='keyboard',
            name='description',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='keyboard',
            name='keycap',
            field=models.ManyToManyField(null=True, to='keyboard.keycap'),
        ),
        migrations.AddField(
            model_name='keyboard',
            name='model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='keyboard.switche'),
        ),
        migrations.AlterField(
            model_name='keyboard',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]