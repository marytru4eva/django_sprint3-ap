from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        # Добавляем поле image в модель Post
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(
                blank=True,
                upload_to='post_images',
                verbose_name='Изображение'
            ),
        ),
        # Создаем модель Comment
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('created_at', models.DateTimeField(
                    auto_now_add=True,
                    verbose_name='Добавлено'
                )),
                ('author', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='comments',
                    to='auth.user',
                    verbose_name='Автор комментария'
                )),
                ('post', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='comments',
                    to='blog.post',
                    verbose_name='Публикация'
                )),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['created_at'],
            },
        ),
    ]
