from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import *
from .forms import CustomUserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware.csrf import get_token
from django.forms.models import model_to_dict


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrf_token': token})


@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return JsonResponse({
                'message': '회원가입이 성공적으로 완료되었습니다.',
                'user_id': user.id
            })
        else:

            return JsonResponse({'error': 'Invalid request.'}, status=400)
    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return JsonResponse({
                'message': '로그인이 성공적으로 완료되었습니다.',
                'user_id': user.id,
                'access_token': access_token,
            })
        else:
            return JsonResponse({'error': 'Invalid credentials.'}, status=401)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({'message': '로그아웃이 성공적으로 완료되었습니다.'})


@csrf_exempt
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_course(request, course_id):
    course = Course.objects.get(id=course_id)
    user_id = request.data.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        course.likes.add(user)
        course.dislikes.remove(user)
        return JsonResponse({}, status=201)
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)


@csrf_exempt
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def dislike_course(request, course_id):
    course = Course.objects.get(id=course_id)
    user_id = request.data.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        course.dislikes.add(user)
        course.likes.remove(user)
        return JsonResponse({}, status=202)
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)


@csrf_exempt
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def check_course_like(request, course_id):
    course = Course.objects.get(id=course_id)
    user_id = request.data.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        if user in course.likes.all():
            check = 1
        else:
            check = 0
        return JsonResponse({'check': check})
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)

# todo 작동 안함


@csrf_exempt
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def user_wishlist(request):
    user_id = request.data.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        interests = user.userprofile.interests.all()
        wishlist = []
        for interest in interests:
            wishlist.append({
                'id': interest.id,
                'courses': {
                    'course_id': interest.id,
                    'course_name': interest.title,
                }
            })
        return JsonResponse(wishlist, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)


def index(request):
    series_list = Series.objects.all()
    return render(request, 'courses/index.html', {'series_list': series_list})


def series(request):
    series_list = Series.objects.all()
    return render(request, 'courses/series/index.html', {'series_list': series_list})


def series_course(request, series_id):
    """
    시리즈에 해당하는 코스 조회 (SeriesCourse model)
    """
    series = Series.objects.get(pk=series_id)  # series_id를 가져오면
    tags = series.tags.all()  # series에 들어있는 태그를 모두 가져온다.
    # 코스에는 태그의 고유값을 가져온다.
    courses = Course.objects.filter(tags__in=tags).distinct()

    series_course_info_list = []

    for course in courses:
        course_info = model_to_dict(course)  # 객체 import
        series_course_info_list.append(course_info)

    context = {
        'series': series,
        'courses': courses,
        'tags': tags,
        'series_course': series_course_info_list
    }

    # print(context)
    return render(request, 'courses/series_course.html', context)
