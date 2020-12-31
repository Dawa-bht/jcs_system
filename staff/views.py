from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import StaffDetail
from students.models import std_registration_form
from .forms import StaffRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .filters import StaffFilter
import csv


# Home page


def home(request):
    male_seven = std_registration_form.objects.filter(
        standard=7, gender='Male')
    female_seven = std_registration_form.objects.filter(
        standard=7, gender='Female')
    total_seven = std_registration_form.objects.filter(
        standard=7)

    male_eight = std_registration_form.objects.filter(
        standard=8, gender='Male')
    female_eight = std_registration_form.objects.filter(
        standard=8, gender='Female')
    total_eight = std_registration_form.objects.filter(
        standard=8)

    male_nine = std_registration_form.objects.filter(standard=9, gender='Male')
    female_nine = std_registration_form.objects.filter(
        standard=9, gender='Female')
    total_nine = std_registration_form.objects.filter(
        standard=9)

    male_ten = std_registration_form.objects.filter(standard=10, gender='Male')
    female_ten = std_registration_form.objects.filter(
        standard=10, gender='Female')
    total_ten = std_registration_form.objects.filter(
        standard=10)

    male_eleven = std_registration_form.objects.filter(
        standard=11, gender='Male')
    female_eleven = std_registration_form.objects.filter(
        standard=11, gender='Female')
    total_eleven = std_registration_form.objects.filter(
        standard=11)

    male_twelve = std_registration_form.objects.filter(
        standard=12, gender='Male')
    female_twelve = std_registration_form.objects.filter(
        standard=12, gender='Female')
    total_twelve = std_registration_form.objects.filter(
        standard=12)

    male = std_registration_form.objects.filter(gender='Male')
    female = std_registration_form.objects.filter(gender='Female')
    total = std_registration_form.objects.all()

    # staff-adm
    male_adm = StaffDetail.objects.filter(
        category='Administration', gender='Male')
    female_adm = StaffDetail.objects.filter(
        category='Administration', gender='Female')
    total_adm = StaffDetail.objects.filter(category='Administration')

    # staff_teachers
    male_teacher = StaffDetail.objects.filter(
        category='Teaching Staff', gender='Male')
    female_teacher = StaffDetail.objects.filter(
        category='Teaching Staff', gender='Female')
    total_teacher = StaffDetail.objects.filter(category='Teaching Staff')

    # staff_non_teachers
    male_non_teacher = StaffDetail.objects.filter(
        category='Non Teaching Staff', gender='Male')
    female_non_teacher = StaffDetail.objects.filter(
        category='Non Teaching Staff', gender='Female')
    total_non_teacher = StaffDetail.objects.filter(
        category='Non Teaching Staff')

    # support staff
    male_support_staff = StaffDetail.objects.filter(
        category='Supporting Staff', gender='Male')
    female_support_staff = StaffDetail.objects.filter(
        category='Supporting Staff', gender='Female')
    total_support_staff = StaffDetail.objects.filter(
        category='Supporting Staff')

    # Total Staff
    male_staff = StaffDetail.objects.filter(gender='Male')
    female_staff = StaffDetail.objects.filter(gender='Female')
    total_staff = StaffDetail.objects.all()

    return render(request, 'home.html',
                  {'male_seven': male_seven, 'female_seven': female_seven, 'total_seven': total_seven,
                   'male_eight': male_eight, 'female_eight': female_eight, 'total_eight': total_eight,
                   'male_nine': male_nine, 'female_nine': female_nine, 'total_nine': total_nine,
                   'male_ten': male_ten, 'female_ten': female_ten, 'total_ten': total_ten,
                   'male_eleven': male_eleven, 'female_eleven': female_eleven, 'total_eleven': total_eleven,
                   'male_twelve': male_twelve, 'female_twelve': female_twelve, 'total_twelve': total_twelve,
                   'male': male, 'female': female, 'total': total,

                   'male_adm': male_adm, 'female_adm': female_adm, 'total_adm': total_adm,
                   'male_teacher': male_teacher, 'female_teacher': female_teacher, 'total_teacher': total_teacher,
                   'male_non_teacher': male_non_teacher, 'female_non_teacher': female_non_teacher, 'total_non_teacher': total_non_teacher,
                   'male_support_staff': male_support_staff, 'female_support_staff': female_support_staff, 'total_support_staff': total_support_staff,
                   'male_staff': male_staff, 'female_staff': female_staff, 'total_staff': total_staff,
                   })

# about page


def about(request):
    return render(request, 'about.html')

# Contact page


def contact(request):
    return render(request, "contact.html")

# Exporting to csv


@ login_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="staff_data.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'EMPLOYEE ID', 'NAME', 'GENDER', 'DATE OF BIRTH', 'CID',
        'CATEGORY', 'POSITION TITLE', 'POSITION LEVEL', 'GRADE', 'APPOINTMENT DATE',
        'JOINING DATE TO SCHOOL', 'TRANSFERED FROM', 'EMPLOYEMENT TYPE',
        'NATIONALITY', 'SUBJECT', 'QUALIFICATION', 'CONTACT NUMBER', 'EMAIL',
        'PERMANENT ADDRESS'
    ])
    staff = StaffDetail.objects.all().order_by('category')
    for staff in staff:
        writer.writerow([
            staff.Employee_ID, staff.name, staff.gender, staff.date_of_birth, staff.CID,
            staff.category, staff.position_title, staff.position_level, staff.grade,
            staff.appointment_date,
            staff.joining_date_of_present_school, staff.transfered_from, staff.Employment_type,
            staff.nationality, staff.subject, staff.qualification, staff.contact_number, staff.email,
            staff.permanent_address])
    return response

# Staff Registration


@ login_required
def add_staff(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST or None, request.FILES)
        if form.is_valid():
            addstaff = form.save(commit=False)
            addstaff.user = request.user
            form.save()
            messages.success(request, 'Staff added successfully!')
            return render(request, 'staff/register_staff.html', {'form': form})
        else:
            messages.error(request,
                           'Could not add the staff. Please check the errors below.')
            return render(request, 'staff/register_staff.html', {'form': form})

    else:
        form = StaffRegistrationForm()
    return render(request, 'staff/register_staff.html', {'form': form})

# Authentication
# Login user


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(
                request, 'Username and password didnot match. Try again!')
            return render(request, 'login.html', {'form': AuthenticationForm()})
        else:
            login(request, user)
            return redirect('home')

# Logout user


@ login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

# Administration home page


def adm(request):
    male = StaffDetail.objects.filter(category='Administration', gender='Male')
    female = StaffDetail.objects.filter(
        category='Administration', gender='Female')
    total = StaffDetail.objects.filter(category='Administration')
    all_field = StaffDetail.objects.filter(
        category='Administration').order_by('name')
    myFilter = StaffFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 10)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'staff/administration.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total

                   })

# View Administration


def adm_detail(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    return render(request, 'staff/staff_detail.html', {'staff': staff})

# Edit administration detail


@ login_required
def edit_adm_detail(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    if request.method == 'POST':
        form = StaffRegistrationForm(
            request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff detail updated successfully!')
            return render(request, 'staff/edit_staff_detail.html', {'staff': staff, 'form': form})
        else:
            messages.error(request, 'Staff detail update failed. Try again!')
            return render(request, 'staff/edit_staff_detail.html', {'staff': staff, 'form': form})
    else:
        form = StaffRegistrationForm(instance=staff)
        return render(request, 'staff/edit_staff_detail.html', {'staff': staff, 'form': form})

# Delete administration Detail


@ login_required
def delete_adm(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    staff.delete()
    return redirect('staff:adm')

# Teacher home page


def teacher(request):
    male = StaffDetail.objects.filter(category='Teaching Staff', gender='Male')
    female = StaffDetail.objects.filter(
        category='Teaching Staff', gender='Female')
    total = StaffDetail.objects.filter(category='Teaching Staff')
    all_field = StaffDetail.objects.filter(
        category='Teaching Staff').order_by('name')
    myFilter = StaffFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 10)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'staff/teacher.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total
                   })
# View Teacher


def teacher_detail(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    return render(request, 'staff/staff_detail.html', {'staff': staff})

# Edit Teacher detail


@ login_required
def edit_teacher_detail(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    if request.method == 'POST':
        form = StaffRegistrationForm(
            request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff detail updated successfully!')
            return render(request, 'staff/edit_staff_detail.html', {'staff': staff, 'form': form})
        else:
            messages.error(request, 'Staff detail update failed. Try again!')
            return render(request, 'staff/edit_staff_detail.html', {'staff': staff, 'form': form})
    else:
        form = StaffRegistrationForm(instance=staff)
        return render(request, 'staff/edit_staff_detail.html', {'staff': staff, 'form': form})

# Delete Teacher Detail


@ login_required
def delete_teacher(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    staff.delete()
    return redirect('staff:teacher')


# Non Teacher home page


def non_teacher(request):
    male = StaffDetail.objects.filter(
        category='Non Teaching Staff', gender='Male')
    female = StaffDetail.objects.filter(
        category='Non Teaching Staff', gender='Female')
    total = StaffDetail.objects.filter(category='Non Teaching Staff')
    all_field = StaffDetail.objects.filter(
        category='Non Teaching Staff').order_by('name')
    myFilter = StaffFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 10)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'staff/non_teacher.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total
                   })
# View Non Teacher


def non_teacher_detail(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    return render(request, 'staff/staff_detail.html', {'staff': staff})

# Edit Non Teacher detail


@ login_required
def edit_non_teacher_detail(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    if request.method == 'POST':
        form = StaffRegistrationForm(
            request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff detail updated successfully!')
            return render(request, 'staff/edit_staff_detail.html', {'staff': staff, 'form': form})
        else:
            messages.error(request, 'Staff detail update failed. Try again!')
            return render(request, 'staff/edit_staff_detail.html', {'staff': staff, 'form': form})
    else:
        form = StaffRegistrationForm(instance=staff)
        return render(request, 'staff/edit_staff_detail.html', {'staff': staff, 'form': form})

# Delete Non Teacher Detail


@ login_required
def delete_non_teacher(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    staff.delete()
    return redirect('staff:non_teacher')

# Support Staff home page


def support_staff(request):
    male = StaffDetail.objects.filter(
        category='Supporting Staff', gender='Male')
    female = StaffDetail.objects.filter(
        category='Supporting Staff', gender='Female')
    total = StaffDetail.objects.filter(category='Supporting Staff')
    all_field = StaffDetail.objects.filter(
        category='Supporting Staff').order_by('name')
    myFilter = StaffFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 10)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'staff/support_staff.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total
                   })
# View Teacher


def support_staff_detail(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    return render(request, 'staff/staff_detail.html', {'staff': staff})

# Edit Teacher detail


@ login_required
def edit_support_staff_detail(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    if request.method == 'POST':
        form = StaffRegistrationForm(
            request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff detail updated successfully!')
            return render(request, 'staff/edit_staff_detail.html', {'staff': staff, 'form': form})
        else:
            messages.error(request, 'Staff detail update failed. Try again!')
            return render(request, 'staff/edit_staff_detail.html', {'staff': staff, 'form': form})
    else:
        form = StaffRegistrationForm(instance=staff)
        return render(request, 'staff/edit_staff_detail.html', {'staff': staff, 'form': form})

# Delete Teacher Detail


@ login_required
def delete_support_staff(request, Emp_id):
    staff = get_object_or_404(StaffDetail, pk=Emp_id)
    staff.delete()
    return redirect('staff:support_staff')
