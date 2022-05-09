# Generated by Django 3.2.13 on 2022-05-09 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='زمان بروزرسانی')),
                ('name', models.CharField(max_length=50, verbose_name='نام تیم')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='teams', verbose_name='لوگوی تیم')),
            ],
            options={
                'verbose_name': 'تیم',
                'verbose_name_plural': 'تیم',
            },
        ),
    ]
