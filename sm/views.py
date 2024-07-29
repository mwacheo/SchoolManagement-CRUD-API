from django.shortcuts import render
from rest_framework import generics
from .models import Teacher,Subject
from .serializers import TeacherSerializer,SubjectSerializer

# Create your views here.

class TeacherListCreateView (generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherRetrieveUpdateDestroyView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    

class SubjectListCreateView (generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectRetrieveUpdateDestroyView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


