# Generated by Django 3.2 on 2023-10-29 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0007_auto_20231020_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('image', models.ImageField(upload_to='school/', verbose_name='фото')),
            ],
        ),
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ('name',), 'verbose_name': 'Школа', 'verbose_name_plural': 'Школы'},
        ),
        migrations.RemoveField(
            model_name='kindergartens',
            name='album',
        ),
        migrations.RemoveField(
            model_name='school',
            name='album',
        ),
        migrations.AlterField(
            model_name='coursealbum',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album', to='education.course', verbose_name='Курсы'),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.AddField(
            model_name='schoolalbum',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album', to='education.school', verbose_name='Школы'),
        ),
    ]
