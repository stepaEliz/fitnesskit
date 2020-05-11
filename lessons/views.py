from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Lesson
from .serializers import LessonSerializer


class LessonView(APIView):
    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response({"lessons": serializer.data})
