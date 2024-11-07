from rest_framework import serializers
from .models import Question,StudentDetail  # Make sure to import your Question model

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'option_a', 'option_b']  # List all fields you want to serialize
        
    
class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetail
        fields = "__all__"
        