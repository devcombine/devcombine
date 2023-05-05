from django.db import models
from django.contrib.auth.models import User

# https://wayhome25.github.io/django/2017/06/20/selected_related_prefetch_related/


class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Series(models.Model):
    # Series:Tag = 1:N
    ###############################################
    title = models.CharField(max_length=300)
    tags = models.ManyToManyField(Tag, through='SeriesTag')
    ###############################################
    subtitle = models.CharField(max_length=300, null=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class SeriesTag(models.Model):
    # Series:Tag = 1:ㅡ
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    series_id = models.ForeignKey(Series, on_delete=models.CASCADE)


class Course(models.Model):
    # Course
    ##############################################
    title = models.CharField(max_length=100) 
    
    # tag를 등록하는 객체
    tags = models.ManyToManyField(Tag, through='CourseTag') # 필수값
    ##############################################
    instructor = models.CharField(max_length=32, null=True)
    description = models.TextField(null=True)
    site = models.CharField(max_length=32, null=True)
    url = models.URLField(max_length=500, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    rating = models.DecimalField(
        max_digits=3, decimal_places=2, null=True, blank=True)
    thumbnail_url = models.URLField(max_length=500, null=True, blank=True)
    is_package = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)
    enrollment_count = models.IntegerField(default=0)

    # 찜기능
    likes = models.ManyToManyField(User, related_name='liked_courses')
    dislikes = models.ManyToManyField(User, related_name='disliked_courses')

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
