from rest_framework import serializers
from .models import Lesson, Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['short_name', 'name', 'position', 'imageUrl']


class LessonSerializer(serializers.ModelSerializer):
    teacher_v2 = TeacherSerializer()

    class Meta:
        model = Lesson
        fields = ['name', 'description', 'place', 'teacher', 'startTime', 'endTime', 'weekDay', 'appointment_id', 'service_id', 'pay', 'appointment', 'teacher_v2', 'color', 'availability']
