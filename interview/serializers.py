from rest_framework import serializers
from interview.models import shedule
 
class SheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = shedule
        fields = "__all__"