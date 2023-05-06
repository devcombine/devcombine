# Generated by Django 4.2 on 2023-05-06 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('subtitle', models.CharField(max_length=300, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('is_main', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SeriesTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.series')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.tag')),
            ],
        ),
        migrations.AddField(
            model_name='series',
            name='tags',
            field=models.ManyToManyField(through='series.SeriesTag', to='courses.tag'),
        ),
    ]
