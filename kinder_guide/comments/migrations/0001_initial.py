# Generated by Django 3.2 on 2023-10-18 15:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='ReviewSchool',
            fields=[
                ('review_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='comments.review')),
                ('review_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='education.school')),
            ],
            bases=('comments.review',),
        ),
        migrations.CreateModel(
            name='ReviewKindergarten',
            fields=[
                ('review_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='comments.review')),
                ('review_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='education.kindergartens')),
            ],
            bases=('comments.review',),
        ),
        migrations.CreateModel(
            name='ReviewCourse',
            fields=[
                ('review_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='comments.review')),
                ('review_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='education.course')),
            ],
            bases=('comments.review',),
        ),
    ]
