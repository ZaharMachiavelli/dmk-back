from django.urls import path, include
from . import views
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
# router.register(r'dmk', StatisticsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profession', get_cx),
    path('professions', ProfessionView.as_view()),
    # path('stat/<int:year>/', StatisticView.as_view()),
    path('skills', SkillsView.as_view()),
    path('courses', CourseView.as_view()),
    path('courses/<slug:slug_id>', get_course),
    path('user', UserView.as_view()),
    path('stat/<int:year>', StatisticView.as_view()),
    # path('hype', get_hype)
    # path('getprofession', CheckDiscipline.as_view())
    # path('schedule/cheese/', FuckMyCheese.as_view()),
    # path('<int:art_id>/', views.ArticleDetailView.as_view())
]
