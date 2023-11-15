# Generated by Django 3.2 on 2023-11-15 14:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='ReviewKindergarten',
            fields=[
                ('review_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='comments.review')),
            ],
            options={
                'verbose_name': 'Отзыв детского сада',
                'verbose_name_plural': 'Отзывы детских садов',
            },
            bases=('comments.review',),
        ),
        migrations.CreateModel(
            name='ReviewSchool',
            fields=[
                ('review_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='comments.review')),
            ],
            options={
                'verbose_name': 'Отзыв школы',
                'verbose_name_plural': 'Отзывы школ',
            },
            bases=('comments.review',),
        ),
    ]
