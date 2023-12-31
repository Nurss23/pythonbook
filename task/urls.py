from django.urls import path, include
from task.views.task import *
from task.views.add_view import *
from rest_framework import routers

app_name = 'task'

router = routers.DefaultRouter()
router.register(r'task-viewset', TaskViewSet)

urlpatterns = [
    path('detail/<int:pk>/', TaskDetailAPIView.as_view(), name="task-detail"),
    path('list/', TasksView.as_view(), name='list'),
    # path('answer-detail/<int:pk>/', AnswerDetailAPIView.as_view(), name="answer-detail"),
    # path('answer-list/', AnswersView.as_view(), name='list'),
    path('add-view/<int:task_pk>/', AddViewAPI.as_view(), name='add-view'),
    path('detail-generic/<int:pk>/', TaskGenericDetailAPIView.as_view(), name="task-detail-generic"),   
    path('list-generic/', TasksGenericView.as_view(), name='list-generic'),
    path('task-vs/', include(router.urls)),
]