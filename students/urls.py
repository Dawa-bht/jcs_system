from django.urls import path
from students import views

app_name = 'students'

urlpatterns = [
    # Add student
    path('addstudent', views.add_std, name='add_std'),


    # Disciplinary Issue update
    path('add_disciplinaryissue', views.disciplinaryissue,
         name='disciplinaryissue'),

    # Character certificate update
    path('add_character_certificate', views.charactercertificate,
         name='charactercertificate'),

    # export csv
    path('export_csv', views.export_csv, name='export_csv'),


    # Class Seven
    path('seven/', views.seven, name='seven'),
    path('seven/<str:std_code>/', views.std_detail_seven, name='std_detail_seven'),
    path('seven/edit/<str:std_code>/',
         views.edit_std_seven, name='edit_std_seven'),
    path('seven/delete/<str:std_code>/',
         views.delete_std_seven, name='delete_std_seven'),

    # Class Eight
    path('eight/', views.eight, name='eight'),
    path('eight/<str:std_code>/', views.std_detail_eight, name='std_detail_eight'),
    path('eight/edit/<str:std_code>/',
         views.edit_std_eight, name='edit_std_eight'),
    path('eight/delete/<str:std_code>/',
         views.delete_std_eight, name='delete_std_eight'),

    # Class Nine
    path('nine/', views.nine, name='nine'),
    path('nine/<str:std_code>/', views.std_detail_nine, name='std_detail_nine'),
    path('nine/edit/<str:std_code>/',
         views.edit_std_nine, name='edit_std_nine'),
    path('nine/delete/<str:std_code>/',
         views.delete_std_nine, name='delete_std_nine'),

    # Class Ten
    path('ten/', views.ten, name='ten'),
    path('ten/<str:std_code>/', views.std_detail_ten, name='std_detail_ten'),
    path('ten/edit/<str:std_code>/',
         views.edit_std_ten, name='edit_std_ten'),
    path('ten/delete/<str:std_code>/',
         views.delete_std_ten, name='delete_std_ten'),

    # Class eleven
    path('eleven/', views.eleven, name='eleven'),
    path('eleven/<str:std_code>/', views.std_detail_eleven,
         name='std_detail_eleven'),
    path('eleven/edit/<str:std_code>/',
         views.edit_std_eleven, name='edit_std_eleven'),
    path('eleven/delete/<str:std_code>/',
         views.delete_std_eleven, name='delete_std_eleven'),

    # Class twelve
    path('twelve/', views.twelve, name='twelve'),
    path('twelve/<str:std_code>/', views.std_detail_twelve,
         name='std_detail_twelve'),
    path('twelve/edit/<str:std_code>/',
         views.edit_std_twelve, name='edit_std_twelve'),
    path('twelve/delete/<str:std_code>/',
         views.delete_std_twelve, name='delete_std_twelve'),

]
