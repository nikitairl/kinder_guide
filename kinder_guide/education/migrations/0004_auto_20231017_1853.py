# Generated by Django 3.2 on 2023-10-17 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_auto_20231016_2309'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='course',
            name='telephone',
            field=models.CharField(max_length=250, verbose_name='Телефон'),
        ),
        migrations.RemoveField(
            model_name='course',
            name='underground',
        ),
        migrations.AlterField(
            model_name='kindergartens',
            name='telephone',
            field=models.CharField(max_length=250, verbose_name='Телефон'),
        ),
        migrations.RemoveField(
            model_name='kindergartens',
            name='underground',
        ),
        migrations.AlterField(
            model_name='school',
            name='telephone',
            field=models.CharField(max_length=250, verbose_name='Телефон'),
        ),
        migrations.RemoveField(
            model_name='school',
            name='underground',
        ),
        migrations.AddField(
            model_name='course',
            name='underground',
            field=models.ManyToManyField(related_name='course', to='education.Underground', verbose_name='Языки'),
        ),
        migrations.AddField(
            model_name='kindergartens',
            name='underground',
            field=models.ManyToManyField(related_name='kindergartens', to='education.Underground', verbose_name='Языки'),
        ),
        migrations.AddField(
            model_name='school',
            name='underground',
            field=models.ManyToManyField(related_name='school', to='education.Underground', verbose_name='Языки'),
        ),
    ]
