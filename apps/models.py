from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    STATUS_CHOISES = (
    ('ACTIVE', 'Active'),
    ('ARCHIVED', 'Archived')
    )
    status = models.CharField(max_length=20,choices=STATUS_CHOISES, default='ACTIVE')

    def __str__(self):
        return f"{self.name} ({self.city})"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='subjects')
    
    STATUS_CHOISES = (
    ('ACTIVE', 'Active'),
    ('ARCHIVED', 'Archived'))

    status = models.CharField(max_length=20,choices=STATUS_CHOISES, default='ACTIVE')
    def __str__(self):
        return f"{self.name}"

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=20)
    parent_name = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=15)
    parent_relationship = models.CharField(max_length=50)

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='Students')
    
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('ARCHIVED','Archived'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    
    def __str__(self):
        return f"{self.first_name} ({self.last_name})"
    
class Group(models.Model):
    name = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='groups')

    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('ARCHIVED','Archived'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    students = models.ManyToManyField(Student, related_name='groups', blank=True)
    def __str__(self):
        return f"{self.name}"

class SubscriptionPlan(models.Model):
    
    TYPE_CHOICES = (
        ('INDIVIDUAL', 'Індивідуальні'),
        ('GROUP', 'Групові'),
    )
    name = models.CharField(max_length=150, verbose_name="Назва тарифу")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subscription_plans', verbose_name="Предмет")
    plan_type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Тип занять")
    lessons_count = models.PositiveIntegerField(verbose_name="Кількість занять")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")

    def __str__(self):
        return f"{self.name} ({self.subject.name} - {self.lessons_count} занять)"

class Lesson(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='lessons', verbose_name="Група")
    date = models.DateField(verbose_name="Дата проведення")
    start_time = models.TimeField(verbose_name="Час початку")
    end_time = models.TimeField(verbose_name="Час закінчення")

    def __str__(self):
        return f"Урок {self.group.name} ({self.date} | {self.start_time} - {self.end_time})"        

class Attendance(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='attendances', verbose_name="Урок")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances', verbose_name="Студент")
    is_present = models.BooleanField(default=False, verbose_name="Присутній")
    
    class Meta:
        unique_together = ('lesson', 'student')

    def __str__(self):
        status = "Був" if self.is_present else "Не був"
        return f"{self.student.first_name} - {self.lesson.date} ({status})"

class StudentSubscription(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='subscriptions', verbose_name="Студент")
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.PROTECT, verbose_name="Тарифний план")
    lessons_left = models.PositiveIntegerField(verbose_name="Залишок занять")
    purchase_date = models.DateField(auto_now_add=True, verbose_name="Дата покупки")
    is_active = models.BooleanField(default=True, verbose_name="Активний")

    def __str__(self):
        return f"{self.student.first_name} - {self.plan.name} (Залишилось: {self.lessons_left})"