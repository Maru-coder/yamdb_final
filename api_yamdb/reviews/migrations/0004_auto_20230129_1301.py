# Generated by Django 3.2 on 2023-01-29 10:01

import django.core.validators

from django.db import migrations, models

import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_review_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='rating',
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(error_messages={'valid_number': 'Введите число в диапазоне от 1 до 10'}, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='оценка'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(validators=[reviews.validators.year_validator], verbose_name='Год создания произведения'),
        ),
    ]
