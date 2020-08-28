from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from . import serializers

from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
# Create your views here.

#---------------------------------------------------------------------------------#
# View for the api implementation using viewset
"""class TaskListViewset(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = serializers.TaskListSerializer"""

#----------------------------------------------------------------------------------#
# Implementing API views using generic APIView and mixins
"""class TaskListAPiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = TaskList.objects.all()
    serializer_class = serializers.TaskListSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TaskDetailAPiView(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = TaskList.objects.all()
    serializer_class = serializers.TaskListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)"""

#----------------------------------------------------------------------------------#
# Implementing API views using just the generics without mixins
class TaskGenLCAPIView(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = serializers.TaskListSerializer

class TaskGenRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = serializers.TaskListSerializer
#----------------------------------------------------------------------------------#
# Implementing API using class based view
"""class TaskAPiView(APIView):

    #List all tasks(get) or create(post) all tasks API view

    def get(self, request):
        queryset = TaskList.objects.all()
        serializer = serializers.TaskListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data=request.data
        serializer = serializers.TaskListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPiView(APIView):

    #Retrieve, Update and Delete Class Based API Views(all dealing with details)
    
    def get_object(self, pk):
        try:
            return TaskList.objects.get(pk=pk)
        except TaskList.DoesNotExist:
            return Response({"Error":"Task Does Not Exist"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = serializers.TaskListSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = serializers.TaskListSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response({"Success Message":"Task Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)"""
#----------------------------------------------------------------------------------#
# Implementing API using function based view
"""@csrf_exempt
def task_api_fbview(request):
    if request.method == "GET":
        queryset = TaskList.objects.all()
        serializer = serializers.TaskListSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False) #safe=False allows us to pass the serialized data as a list of dictionaries instead of just dict(json format)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = serializers.TaskListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def task_api_details(request,pk):
    try:
        task = TaskList.objects.get(pk=pk)
    except task.DoesNotExist:
        return JsonResponse({"Error":"Task Does Not Exist"}, status=404)
    if request.method == "GET":
        serializer = serializers.TaskListSerializer(task)
        return JsonResponse(serializer.data, status=200)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = serializers.TaskListSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
            task.delete()
            return JsonResponse({"Success Message":"Task Deleted Successfully"}, status=204)"""

#-----------------------------------------------------------------------------------------------#
def index(request):
    context ={
        'index_text':"Welcome to the Home Page"
    }
    return render(request, 'index.html', context)    

def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()  
            messages.success(request, ("New Task Added!!"))    
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.all()
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks':all_tasks})

def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    
    return redirect('todolist')

def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, ("Task edited successfully"))    
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj':task_obj})

def yes_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()

    return redirect('todolist')

def no_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()

    return redirect('todolist')

def contact(request):
    context ={
        'contact_text':"Welcome to Contact Page"
    }
    return render(request, 'contact.html', context)    

def about(request):
    context ={
        'about_text':"Welcome to About Page"
    }
    return render(request, 'about.html', context) 

def service(request):
    context ={
        'service_text':"Welcome to the Services (Python) Page"
    }    
    return render(request, 'service.html', context)