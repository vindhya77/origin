from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets


class StudentView(viewsets.Viewset):
	def list(self, request):
		queryset = Student.objects.all()
		serializer = StudentSerializer(queryset, many=True)
		return Response(serializer.data)