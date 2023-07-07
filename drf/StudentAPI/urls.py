from django.urls import path

from . import views

urlpatterns = [
    path('', views.student_list_create_view, name='student-list'),
    path('update/<int:pk>/', views.student_update_view, name="student-edit"),
    path('delete/<int:pk>/', views.student_delete_view, name="student-delete"),
    path('<int:pk>/', views.student_detail_view, name="student-detail")
]
