from rest_framework import serializers

from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = [
            'Admission_Number',
            'First_Name',
            'Last_Name',
            'Date_Of_Birth',
            'Date_Joined',
            'Faculty',
            'Department',
            'Course_Name',
            'Year_Of_Study',
            'Unit_Name',
            'Grade'
        ]