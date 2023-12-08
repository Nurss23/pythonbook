from django.urls import path, include
from students.views import *
from students.serializers import *
from rest_framework import routers

app_name = "student"

router = routers.DefaultRouter()
router.register(r'student-viewset', StudentViewSet)

urlpatterns = [
    path('detail/<int:pk>/', StudentDetailAPIView.as_view(), name="student-detail"),
    path('list/', StudentsView.as_view(), name="list"),
    path('detail-generic/<int:pk>/', StudentGenericDetailAPIView.as_view(), name="task-detail-generic"),   
    path('list-generic/', StudentsGenericView.as_view(), name='list-generic'),
    path('student-set/', include(router.urls)),
]