# Generated by Django 3.2.13 on 2022-05-15 10:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='player',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
        migrations.AddField(
            model_name='player',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Update at'),
        ),
    ]
