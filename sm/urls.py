
from .views import TeacherListCreateView,TeacherRetrieveUpdateDestroyView,SubjectListCreateView,SubjectRetrieveUpdateDestroyView
from django.urls import path


urlpatterns = [
    path('teachers/', TeacherListCreateView.as_view(), name='teachers-list-create'),
    path('teachers/<int:pk>/', TeacherRetrieveUpdateDestroyView.as_view(), name='teacher-detail'),
    path('subjects/', SubjectListCreateView.as_view(), name='subject-list-create'),
    path('subjects/<int:pk>/', SubjectRetrieveUpdateDestroyView.as_view(), name='subject-detail'),
   

]



