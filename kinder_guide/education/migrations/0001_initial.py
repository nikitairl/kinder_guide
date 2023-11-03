# Generated by Django 3.2 on 2023-11-03 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Возрастная категория',
                'verbose_name_plural': 'Возрастные категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Округ',
                'verbose_name_plural': 'Округ',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Create',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Творческое занятие',
                'verbose_name_plural': 'Творческие занятия',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Intelligence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Интеллектуальное занятие',
                'verbose_name_plural': 'Интеллектуальные занятия',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Музыкальное занятие',
                'verbose_name_plural': 'Музыкальные занятия',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название школы')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('working_hours', models.CharField(blank=True, max_length=250, null=True, verbose_name='Время работы')),
                ('telephone', models.CharField(max_length=250, unique=True, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='Адрес')),
                ('email', models.EmailField(blank=True, max_length=250, null=True, unique=True, verbose_name='Электронный адрес')),
                ('website', models.URLField(blank=True, null=True, unique=True, verbose_name='Веб-сайт')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена в месяц')),
                ('age', models.CharField(blank=True, max_length=250, null=True, verbose_name='Возраст')),
                ('price_of_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена в год')),
                ('classes', models.CharField(blank=True, max_length=250, null=True, verbose_name='Классы')),
                ('age_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.agecategory', verbose_name='Возрастная категория')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.area', verbose_name='Округ')),
                ('languages', models.ManyToManyField(blank=True, related_name='school', to='education.Language', verbose_name='Языки')),
                ('profile', models.ManyToManyField(blank=True, related_name='school', to='education.Profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Школа',
                'verbose_name_plural': 'Школы',
            },
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Спортивное занятие',
                'verbose_name_plural': 'Спортивные занятия',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Underground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Метро',
                'verbose_name_plural': 'Метро',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SchoolAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='school/', verbose_name='фото')),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album', to='education.school', verbose_name='Школа')),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='underground',
            field=models.ManyToManyField(blank=True, related_name='school', to='education.Underground', verbose_name='Метро'),
        ),
        migrations.CreateModel(
            name='Kindergartens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название детского сада')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('telephone', models.CharField(max_length=250, unique=True, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='Адрес')),
                ('email', models.EmailField(blank=True, max_length=250, null=True, unique=True, verbose_name='Электронный адрес')),
                ('website', models.URLField(blank=True, null=True, unique=True, verbose_name='Веб-сайт')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена в месяц')),
                ('age', models.CharField(blank=True, max_length=250, null=True, verbose_name='Возраст')),
                ('price_of_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена в год')),
                ('working_hours', models.CharField(blank=True, max_length=250, null=True, verbose_name='Время работы')),
                ('group_suze', models.CharField(blank=True, max_length=250, null=True, verbose_name='Размер группы')),
                ('age_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.agecategory', verbose_name='Возрастная категория')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.area', verbose_name='Округ')),
                ('create_dev', models.ManyToManyField(blank=True, related_name='kindergartens', to='education.Create', verbose_name='Творческое развитие')),
                ('intel_dev', models.ManyToManyField(blank=True, related_name='kindergartens', to='education.Intelligence', verbose_name='Интеллектуальное развитие')),
                ('languages', models.ManyToManyField(blank=True, related_name='kindergartens', to='education.Language', verbose_name='Языки')),
                ('music_dev', models.ManyToManyField(blank=True, related_name='kindergartens', to='education.Music', verbose_name='Музыкальное развитие')),
                ('sport_dev', models.ManyToManyField(blank=True, related_name='kindergartens', to='education.Sport', verbose_name='Спортивное развитие')),
                ('underground', models.ManyToManyField(blank=True, related_name='kindergartens', to='education.Underground', verbose_name='Метро')),
            ],
            options={
                'verbose_name': 'Детский сад',
                'verbose_name_plural': 'Детские сады',
            },
        ),
        migrations.CreateModel(
            name='KindergartenAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='kindergartens/', verbose_name='фото')),
                ('kindergarten', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album', to='education.kindergartens', verbose_name='Сад')),
            ],
        ),
        migrations.CreateModel(
            name='Favourites_School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites_users', to='education.school', verbose_name='Учебное заведение в избранном')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites_school', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Избранное - школа',
                'verbose_name_plural': 'Избранное - школы',
            },
        ),
        migrations.CreateModel(
            name='Favourites_Kindergartens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kindergartens', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites_users', to='education.kindergartens', verbose_name='Детский садик в избранном')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites_kindergartens', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Избранное - детский садик',
                'verbose_name_plural': 'Избранное - детские сады',
            },
        ),
    ]
