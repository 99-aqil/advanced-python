from rest_framework import generics

from .models import Student
from .serializers import StudentSerializer

class StudentDetailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # lookup_field = 'pk'

student_detail_view = StudentDetailAPIView.as_view()

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

student_list_create_view = StudentListCreateAPIView.as_view()

class StudentUpdateAPIView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'

student_update_view = StudentUpdateAPIView.as_view()

class StudentDeleteAPIView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

student_delete_view = StudentDeleteAPIView.as_view()

