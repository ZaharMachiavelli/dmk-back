from rest_framework import serializers
from .models import *

class AgregatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agregator
        fields = ['name', 'link']

class CourseSerializer(serializers.ModelSerializer):
    agregator = AgregatorSerializer(read_only=True)
    class Meta:
        model = Course
        fields = ('id', 'slug', 'name', 'description', 'link', 'agregator', 'get_image')

class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'

class ProfessionSerializer(serializers.ModelSerializer):
    first = CourseSerializer(read_only=True, many=True)
    second = CourseSerializer(read_only=True, many=True)
    third = CourseSerializer(read_only=True, many=True)
    forth = CourseSerializer(read_only=True, many=True)
    fifth = CourseSerializer(read_only=True, many=True)
    sixth = CourseSerializer(read_only=True, many=True)
    seventh = CourseSerializer(read_only=True, many=True)
    eigth = CourseSerializer(read_only=True, many=True)
    ninth = CourseSerializer(read_only=True, many=True)
    tenth = CourseSerializer(read_only=True, many=True)
    class Meta:
        model = ProfessionDetail
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionCategory
        fields = ['name', 'tag']

class CategoryViewSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return value.tag

class SkillsSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer(read_only=True)
    class Meta:
        model = ProfessionSkills
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'