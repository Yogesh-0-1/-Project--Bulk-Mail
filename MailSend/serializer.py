from rest_framework import serializers
from .models import details

class mailSeriaizer(serializers.ModelSerializer):
    class Meta:
        model=details
        fields=('Name','PhoneNo','Email','Address','City')