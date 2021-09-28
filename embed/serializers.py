from .models import PharmaDetails, PharmaComponents
from rest_framework import serializers

class PharmaSerializer(serializers.ModelSerializer):
	class Meta:
		model = PharmaDetails
		fields = '__all__'