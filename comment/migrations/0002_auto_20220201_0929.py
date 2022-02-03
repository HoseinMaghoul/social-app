# Generated by Django 3.2.10 on 2022-02-01 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_title'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=-1.0, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='repaly',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='comment.comment'),
        ),
        migrations.CreateModel(
            name='ReplayComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('upload_on', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.CharField(choices=[('0', 'punlished'), ('1', 'pending'), ('2', 'rejeoted')], default=1, max_length=1)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.comment')),
                ('replay', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replaies', to='comment.replaycomment')),
            ],
        ),
    ]
