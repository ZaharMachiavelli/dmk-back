import re
from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from rest_framework.response import Response
from django.http.response import HttpResponse, JsonResponse
from rest_framework.decorators import action
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from collections import Counter
# Create your views here.
# class StatisticsViewSet(viewsets.ModelViewSet):
#     queryset = Statistic.objects.all()
#     serializer_class = StatisticSerializer

#     @action(methods=['get'], detail=True)
#     def year(self, request, pk=None):
#         statistic = Statistic.objects.filter(year=pk)
        
#         return Response({'statistic': StatisticSerializer(statistic).data})

class StatisticView(APIView):
    statistic = None
    def get(self, request, year=None):
        if not year:
            statistic = Statistic.objects.all()
        else:
            statistic = Statistic.objects.filter(year=year)
        serializer = StatisticSerializer(statistic, many=True)
        return Response(serializer.data)

# class ProfessionView(APIView):
#     def get(self, request):
#         professions = Profession.objects.all()
#         serializer = ProfessionSerializer(professions, many=True)
#         return Response({'professions': serializer.data})

class ProfessionView(APIView):
    def get(self, request, id=None):
        print(id)
        if id is None:
            professions = ProfessionDetail.objects.all()
        else: 
            professions = ProfessionDetail.objects.get(pk = id)
        serializer = ProfessionSerializer(professions, many=True)
        return Response(serializer.data)

class SkillsView(APIView):
    def get(self, request):
        skills = ProfessionSkills.objects.all()
        serializer = SkillsSerializer(skills, many=True)
        return Response(serializer.data)

class CourseView(APIView):
    def get(self, request):
        courses  = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    def post(self, request):
        print(request.data)
        favourites = request.data
        courses = Course.objects.filter(pk__in=favourites)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
class CheckDiscipline(APIView):
    def post(self, request):
        disciplines = JSONParser().parse(request)
        professions = ProfessionDetail.objects.all()
        result = {}
        print ('Пользовательский интерфейс' in professions[0].get_disciplines_list())
        for i in range(len(professions)):
            result[professions[i].tag] = 0
            for v in range(len(disciplines)):
                if disciplines[v] in professions[i].get_disciplines_list():
                    result[professions[i].tag] +=1
        max_val = max(result.values())
        final_dict = {k:v for k,v in result.items() if v == max_val}
        professions = ProfessionDetail.objects.filter(tag__in = final_dict.keys())
        serializer = ProfessionSerializer(professions, many=True)
        return Response(serializer.data)


class UserView(APIView):
    def get(self, request):
        id = request.GET.get('id', 1)
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    

@api_view(['GET'])
def get_cx(request):
    profession_title = str(request.GET.get('p', 'designeer'))
    profession = ProfessionDetail.objects.get(tag = profession_title)
    prof_serializer = ProfessionSerializer(profession)
    return Response({'profession': prof_serializer.data}) #

@api_view(['GET'])
def get_course(request, slug_id):
    print(slug_id)
    course = Course.objects.get(slug = str(slug_id))
    print(course)
    serializer = CourseSerializer(course)
    return Response(serializer.data)


@api_view(['POST'])
def get_hype(request):
    return JsonResponse({'a': 2})


