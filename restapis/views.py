from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student


@api_view()
def home(request):
	student_obj = Student.objects.all()
	serializer = StudentSerializer(student_obj, many=True)
	return Response({"payload":serializer.data})

@api_view(['POST',])
def post_data(request):
	serializer = StudentSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({'status':200})
	return Response({'errors': serializer.errors})


@api_view(['POST',])
def update_data(request, id):
	student_obj = Student.objects.filter(id=id).first()
	if student_obj:
		serializer = StudentSerializer(instance=student_obj, data=request.POST, partial=True)
		import pdb;pdb.set_trace()
		if serializer.is_valid():
			serializer.save()
			return Response({'status':200, "payload": serializer.data})
		return Response({'errors': serializer.errors})
	return Response({'Message': 'Object not found'})


