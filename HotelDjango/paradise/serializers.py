from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['phone_number', 'first_name', 'last_name', 'father_name', 'description']

