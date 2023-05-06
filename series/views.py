from django.forms import model_to_dict
from django.shortcuts import render
from django.db.models import Count

from courses.models import Course
from series.models import Series

# Create your views here.


def main_series(request):
    """
    메인에 노출 시키는 시리즈의 목록만 가져오는 함수
    """
    main_series = Series.objects.filter(
        is_main=True)
    print(main_series)
    context = {
        'main_series': main_series
    }

    return render(request, 'series/index.html', context)


def series_list(request):
    """
    전체 시리즈의 목록을 가져오는 함수
    """
    # test 용
    series_list = Series.objects.all()

    return render(request, 'series/index.html')


def series_course(request, series_id):
    """
    시리즈에 해당하는 코스 조회
    """
    series = Series.objects.get(pk=series_id)
    tags = series.tags.all()            # series에 들어있는 들어있는 태그를 모두 가져온다.
    # 태그값으로 필터링 된 코스를 가져온다.
    courses = Course.objects.filter(tags__in=tags).annotate(
        tag_count=Count('tags')).order_by('-tag_count')

    series_course_info_list = []

    for course in courses:
        course_info = model_to_dict(course)
        series_course_info_list.append(course_info)

    context = {
        'series': series,
        'courses': courses,
        'tags': tags,
        'series_course': series_course_info_list
    }
    # print(context)
    return render(request, 'series/series_course.html', context)