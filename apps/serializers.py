from rest_framework import serializers
from .models import Branch, Subject, Student, Group, SubscriptionPlan, Lesson, Attendance, StudentSubscription

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__'
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
class StudentSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSubscription
        fields = '__all__'                
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

    def validate(self, data):
        group = data.get('group')
        date = data.get('date')
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        if start_time >= end_time:
            raise serializers.ValidationError({"time_error": "Час закінчення має бути пізніше часу початку."})
        
        overlapping_lessons = Lesson.objects.filter(
            group=group,
            date=date,
            start_time__lt=end_time, 
            end_time__gt=start_time  
        )

        if overlapping_lessons.exists():
            raise serializers.ValidationError({"conflict_error": "У цієї групи вже є заняття в цей час! Накладка розкладу."})
        
        return data                                         