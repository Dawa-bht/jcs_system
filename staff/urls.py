from django.urls import path
from staff import views

app_name = 'staff'

urlpatterns = [
    # Add student
    path('addstaff', views.add_staff, name='add_staff'),

    # export csv
    path('export_csv', views.export_csv, name='export_csv'),

    # Administration
    path('adm/', views.adm, name='adm'),
    path('adm/<str:Emp_id>/', views.adm_detail, name='adm_detail'),
    path('adm/edit/<str:Emp_id>/',
         views.edit_adm_detail, name='edit_adm_detail'),
    path('adm/delete/<str:Emp_id>/',
         views.delete_adm, name='delete_adm'),

    # Teaching Staff
    path('teacher/', views.teacher, name='teacher'),
    path('teacher/<str:Emp_id>/', views.teacher_detail, name='teacher_detail'),
    path('teacher/edit/<str:Emp_id>/',
         views.edit_adm_detail, name='edit_teacher_detail'),
    path('teacher/delete/<str:Emp_id>/',
         views.delete_teacher, name='delete_teacher'),

    # Non Teaching Staff
    path('non_teacher/', views.non_teacher, name='non_teacher'),
    path('non_teacher/<str:Emp_id>/',
         views.non_teacher_detail, name='non_teacher_detail'),
    path('teacher/edit/<str:Emp_id>/',
         views.edit_non_teacher_detail, name='edit_non_teacher_detail'),
    path('non_teacher/delete/<str:Emp_id>/',
         views.delete_non_teacher, name='delete_non_teacher'),

    # Support Staff
    path('support_staff/', views.support_staff, name='support_staff'),
    path('support_staff/<str:Emp_id>/',
         views.support_staff_detail, name='support_staff_detail'),
    path('support_staff/edit/<str:Emp_id>/',
         views.edit_support_staff_detail, name='edit_support_staff_detail'),
    path('support_staff/delete/<str:Emp_id>/',
         views.delete_support_staff, name='delete_support_staff'),

]
