# Generated by Django 3.2.10 on 2022-04-24 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kavenegar_api_key', models.CharField(blank=True, max_length=150, null=True, verbose_name='کد API key کاوه نگار')),
                ('kavenegar_sender', models.CharField(blank=True, max_length=150, null=True, verbose_name='فرستنده پیامک کاوه نگار')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'تنظیمات سایت',
            },
        ),
    ]