from .models import PharmaDetails, PharmaComponents
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PharmaSerializer
from rest_framework.permissions import IsAuthenticated


# import requests

# auth_token='kbkcmbkcmbkcbc9ic9vixc9vixc9v'
# hed = {'Authorization': 'Bearer ' + auth_token}
# data = {'app' : 'aaaaa'}

# url = 'https://api.xy.com'
# response = requests.post(url, json=data, headers=hed)
# print(response)
# print(response.json())

class PharmaDetailView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		result_list = []
		pharma_components = PharmaComponents.objects.values('AWBnumber').distinct()
		# import pdb;pdb.set_trace()
		for component in pharma_components:
			component_dict = {'AWBnumber': component['AWBnumber'], 'BeaconList': None}
			pharma_details = PharmaDetails.objects.filter(AWBnumber=component['AWBnumber'])
			serializer = PharmaSerializer(pharma_details, many=True)
			component_dict['BeaconList'] = serializer.data
			result_list.append(component_dict)

		return Response(result_list)
