from django.test import TestCase
from django.utils import timezone
from .models import Branch, Group, Lesson, Subject
from rest_framework.exceptions import ValidationError
from .serializers import LessonSerializer

class LessonConflictTest(TestCase):
    def setUp(self):
        self.branch = Branch.objects.create(name="Test Branch", city="Lviv")
        self.subject = Subject.objects.create(name="Math", branch=self.branch)
        self.group = Group.objects.create(name="Alpha", branch=self.branch)

    def test_lesson_overlap_conflict(self):
        """Перевірка, що система не дозволяє створити уроки, які накладаються"""
        date = timezone.now().date()
        

        Lesson.objects.create(
            date=date, start_time="10:00:00", end_time="11:00:00",
            group=self.group, subject=self.subject
        )

        data = {
            "date": date,
            "start_time": "10:30:00",
            "end_time": "11:30:00",
            "group": self.group.id,
            "subject": self.subject.id
        }
        
        serializer = LessonSerializer(data=data)
    
        self.assertFalse(serializer.is_valid())
        self.assertIn('conflict_error', serializer.errors)