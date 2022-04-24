# Generated by Django 3.2.10 on 2022-04-23 10:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Create Timestamp')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Update Timestamp')),
                ('name', models.CharField(max_length=150, verbose_name='نام تیم')),
                ('logo', models.ImageField(blank=True, help_text='لطفا تصویری با عرض y و ارتفاع x پیکسل بارگذاری نمایید.', null=True, upload_to='events/teams', verbose_name='لوگو')),
            ],
            options={
                'verbose_name': 'تیم',
                'verbose_name_plural': 'تیم',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Create Timestamp')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Update Timestamp')),
                ('datetime', django_jalali.db.models.jDateTimeField(null=True, verbose_name='زمان برگزاری')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات رویداد')),
                ('image', models.ImageField(blank=True, default='events/default.jpg', help_text='لطفا تصویری با عرض y و ارتفاع x پیکسل بارگذاری نمایید.', null=True, upload_to='events', verbose_name='تصویر رویداد')),
                ('total_capacity', models.PositiveIntegerField(verbose_name='ظرفیت کل')),
                ('remaining_capacity', models.PositiveIntegerField(editable=False, verbose_name='ظرفیت باقیمانده')),
                ('price', models.PositiveIntegerField(default=0, help_text='قیمت به تومان', verbose_name='قیمت')),
                ('is_available', models.BooleanField(default=True, help_text='زمانی که ظرفیت رویداد به پایان برسد یا ادمین سایت این گزینه را لغو کند، امکان خرید بلیط برای این رویداد غیرفعال خواهد شد.', verbose_name='قابل استفاده بودن')),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='away_team_set', to='events.team', verbose_name='تیم مهمان')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='home_team_set', to='events.team', verbose_name='تیم میزبان')),
            ],
            options={
                'verbose_name': 'رویداد',
                'verbose_name_plural': 'رویداد',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Create Timestamp')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Update Timestamp')),
                ('full_name', models.CharField(blank=True, max_length=150, verbose_name='نام و نام خانوادگی')),
                ('phone', models.CharField(blank=True, max_length=14, null=True, validators=[django.core.validators.RegexValidator(message='Please Enter a Valid Phone Number!', regex='^(0)?9\\d{9}$')], verbose_name='شماره موبایل')),
                ('national_code', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message="National code isn't valid!", regex='^(?!(\\d)\x01{9})\\d{10}$')], verbose_name='کدملی')),
                ('is_used', models.BooleanField(default=False, help_text='زمانی که بلیط تحویل ورزشگاه شد، این فیلد باید توسط ادمین تغییر کند.', verbose_name='استفاده شده')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event', verbose_name='رویداد')),
            ],
            options={
                'verbose_name': 'بلیط',
                'verbose_name_plural': 'بلیط',
                'unique_together': {('event', 'national_code')},
            },
        ),
    ]