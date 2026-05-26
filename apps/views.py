from rest_framework import viewsets
from .models import Branch, Subject, Student, Group, SubscriptionPlan, Lesson, Attendance, StudentSubscription 
from .serializers import (
    BranchSerializer, SubjectSerializer, StudentSerializer, 
    GroupSerializer, SubscriptionPlanSerializer, LessonSerializer, 
    AttendanceSerializer, StudentSubscriptionSerializer
)
from .permissions import IsAdminOrReadOnly


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdminOrReadOnly]

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all().select_related('branch')
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminOrReadOnly]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().select_related('branch')
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrReadOnly]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().select_related('branch').prefetch_related('students')
    serializer_class = GroupSerializer
    permission_classes = [IsAdminOrReadOnly]

class SubscriptionPlanViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionPlan.objects.all().select_related('branch')
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [IsAdminOrReadOnly]

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all().select_related('group', 'subject')
    serializer_class = LessonSerializer
    permission_classes = [IsAdminOrReadOnly]

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all().select_related('lesson', 'student')
    serializer_class = AttendanceSerializer
    permission_classes = [IsAdminOrReadOnly] 

class StudentSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = StudentSubscription.objects.all().select_related('student', 'plan')
    serializer_class = StudentSubscriptionSerializer
    permission_classes = [IsAdminOrReadOnly]