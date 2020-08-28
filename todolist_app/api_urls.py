from django.urls import path, include
from . import views

#-------------------------------------------------#
# Implementation of the url routing when using viewset
"""from rest_framework import routers
router = routers.DefaultRouter()
router.register('tasks', views.TaskListViewset)

urlpatterns = [
    path('', include(router.urls)),
]"""

#---------------------------------------------------#
"""# Implementation of the url routing using function based views
urlpatterns = [
    path('tasks/', views.task_api_fbview, name="task_api_fbview"),
    path('tasks/<int:pk>/', views.task_api_details, name="task_api_details"),
]"""

#-----------------------------------------------------#
# Implementation of the url routing using class based views
"""urlpatterns = [
    path('tasks/', views.TaskAPiView.as_view(), name="task_api_cbview"),
    path('tasks/<int:pk>/', views.TaskDetailAPiView.as_view(), name="task_api_cbdetails"),
]"""

#---------------------------------------------------#
# Implementation of routing using generic API views and mixins
"""urlpatterns = [
    path('tasks/', views.TaskListAPiView.as_view(), name="task_api_generic_list"),
    path('tasks/<int:pk>/', views.TaskDetailAPiView.as_view(), name="task_api_generic_detail"),
]"""

#---------------------------------------------------#
# Implementing API views using only generic Views. NO MIXINS
urlpatterns = [
    path('generic/tasks/', views.TaskGenLCAPIView.as_view()),
    path('generic/tasks/<int:pk>/', views.TaskGenRUDAPIView.as_view()),
]