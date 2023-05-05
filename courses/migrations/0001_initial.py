# Generated by Django 4.2 on 2023-05-05 06:45

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
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="Series",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_date", models.DateField(null=True)),
                ("end_date", models.DateField(null=True)),
                (
                    "interests",
                    models.ManyToManyField(
                        related_name="interested_users", to="courses.course"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SeriesTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "series_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="courses.series"
                    ),
                ),
                (
                    "tag_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="courses.tag"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="series",
            name="tags",
            field=models.ManyToManyField(through="courses.SeriesTag", to="courses.tag"),
        ),
        migrations.CreateModel(
            name="CourseTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "course_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="courses.course"
                    ),
                ),
                (
                    "tag_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="courses.tag"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="tags",
            field=models.ManyToManyField(through="courses.CourseTag", to="courses.tag"),
        ),
    ]
