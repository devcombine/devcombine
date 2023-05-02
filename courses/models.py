from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=300)
    instructor = models.CharField(max_length=200)
    description = models.TextField()
    site = models.CharField(max_length=400)
    url = models.URLField(max_length=500)
    price = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    thumbnail_url = models.URLField(max_length=500, null=True, blank=True)
    is_package = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)
    enrollment_count = models.IntegerField(default=0)
    upload_date = models.DateField(auto_now_add=False, null=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=False, null=True)
    end_date = models.DateField(auto_now_add=False, null=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f'{self.user.username} - {self.course.title}'


class Series(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title

class SeriesCourse(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('series', 'course')

    def __str__(self):
        return f'{self.series.title} - {self.course.title}'