from django.db import models
from django.contrib.auth.models import User

# https://wayhome25.github.io/django/2017/06/20/selected_related_prefetch_related/


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Series(models.Model):
    # Series:Tag = 1:N
    title = models.CharField(max_length=300)
    tags = models.ManyToManyField(Tag, through='SeriesTag')

    def __str__(self):
        return self.title


class SeriesTag(models.Model):
    # Series:Tag = N:1
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    series_id = models.ForeignKey(Series, on_delete=models.CASCADE)


class Course(models.Model):
    # Course
    title = models.CharField(max_length=300)
    # tag를 등록하는 객체
    tags = models.ManyToManyField(Tag, through='CourseTag')

    def __str__(self):
        return self.title


class CourseTag(models.Model):
    # CourseTag - Course : Tag
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.ManyToManyField(Course, related_name='interested_users')
    start_date = models.DateField(auto_now_add=False, null=True)
    end_date = models.DateField(auto_now_add=False, null=True)

#    def __str__(self):
#        return f'{self.user.username} - {self.interests.title}'
