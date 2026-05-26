from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchViewSet, SubjectViewSet, StudentViewSet, GroupViewSet, SubscriptionPlanViewSet, LessonViewSet, AttendanceViewSet, StudentSubscriptionViewSet

router = DefaultRouter()

router.register(r'branches', BranchViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'students', StudentViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'subscription-plans', SubscriptionPlanViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'student-subscriptions', StudentSubscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]