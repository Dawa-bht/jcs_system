from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import std_registration_form, DisciplinaryIssue, CharacterCertificate
from .forms import StdRegistration, DisciplinaryIssueform, CharacterCertificateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .filters import StudentFilter
import csv
from staff.models import StaffDetail
from staff.forms import StaffRegistrationForm

# Main home page


def home(request):
    male_seven = std_registration_form.objects.filter(
        standard=7, gender='Male')
    female_seven = std_registration_form.objects.filter(
        standard=7, gender='Female')
    total_seven = std_registration_form.objects.filter(standard=7)

    male_eight = std_registration_form.objects.filter(
        standard=8, gender='Male')
    female_eight = std_registration_form.objects.filter(
        standard=8, gender='Female')
    total_eight = std_registration_form.objects.filter(standard=8)

    male_nine = std_registration_form.objects.filter(standard=9, gender='Male')
    female_nine = std_registration_form.objects.filter(
        standard=9, gender='Female')
    total_nine = std_registration_form.objects.filter(standard=9)

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

    # staff_adm
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


# Student Registration

@login_required
def add_std(request):
    if request.method == 'POST':
        form = StdRegistration(request.POST or None, request.FILES)
        if form.is_valid():
            addstd = form.save(commit=False)
            addstd.user = request.user
            form.save()
            messages.success(request, 'Student added successfully!')
            return render(request, 'students/add_std.html', {'form': form})
        else:
            messages.error(request,
                           'Could not add the student. Please check the errors below.')
            return render(request, 'students/add_std.html', {'form': form})

    else:
        form = StdRegistration()
    return render(request, 'students/add_std.html', {'form': form})

# Disciplinary Issue update


@ login_required
def disciplinaryissue(request):
    if request.method == 'POST':
        form = DisciplinaryIssueform(request.POST or None)
        if form.is_valid():
            addstd = form.save(commit=False)
            addstd.user = request.user
            form.save()
            messages.success(request, 'Disciplinary issue added successfully!')
            return render(request, 'students/disciplinaryissue.html', {'form': form})
        else:
            messages.error(request,
                           'Error: Could not add disciplinary issue!')
            return render(request, 'students/disciplinaryissue.html', {'form': form})
    else:
        form = DisciplinaryIssueform()
    return render(request, 'students/disciplinaryissue.html', {'form': form})

# Character certificate update


@ login_required
def charactercertificate(request):
    if request.method == 'POST':
        form = CharacterCertificateForm(request.POST or None)
        if form.is_valid():
            addstd = form.save(commit=False)
            addstd.user = request.user
            form.save()
            messages.success(
                request, 'Character certificate added successfully!')
            return render(request, 'students/charactercertificate.html', {'form': form})
        else:
            messages.error(request,
                           'Error: Could not add Character certificate of the student!')
            return render(request, 'students/charactercertificate.html', {'form': form})
    else:
        form = CharacterCertificateForm()
    return render(request, 'students/charactercertificate.html', {'form': form})

# Exporting to csv


@ login_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="student_data.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'STUDENT CODE',
        'NAME',
        'GENDER',
        'STANDARD',
        'SECTION',
        'STREAM',
        'DATE OF BIRTH',
        'ADMISSION NUMBER',
        'DATE OF ADMISSION',
        'EMAIL',
        'CID',
        'CLASS TEACHER',
        'PREVIOUS SCHOOL',
        'MOBILE NUMBER',
        'PERMANENT ADDRESS',
        'BOARDER/DAYSCHOLAR',
        'REGULAR/REPEATER',
        'FATHER NAME',
        'MOTHER NAME',
        'FATHER OCCUPATION',
        'MOTHER OCCUPATION',
        'PARENTS MOBILE NUMBER'
    ])
    std = std_registration_form.objects.all().order_by('standard')
    for std in std:
        writer.writerow([
            std.student_code,
            std.name,
            std.gender,
            std.standard,
            std.section,
            std.Stream,
            std.date_of_birth,
            std.admission_no,
            std.date_of_admission,
            std.email,
            std.CID,
            std.class_teacher,
            std.previous_school,
            std.mobile_number,
            std.permanent_address,
            std.BoarderOrDayscholar,
            std.RegularOrRepeater,
            std.father_name,
            std.mother_name,
            std.fathers_occupation,
            std.mothers_occupation,
            std.parents_mobile_number])
    return response

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
# class seven home page


def seven(request):
    male = std_registration_form.objects.filter(standard=7, gender='Male')
    female = std_registration_form.objects.filter(standard=7, gender='Female')
    total = std_registration_form.objects.filter(standard=7)
    all_field = std_registration_form.objects.filter(
        standard=7).order_by('name')
    myFilter = StudentFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 15)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'students/seven.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total
                   })

# class seven student detail


def std_detail_seven(request, std_code):
    std = get_object_or_404(std_registration_form, pk=std_code)
    disissue = DisciplinaryIssue.objects.filter(Student=std)
    character_certificate = CharacterCertificate.objects.filter(Student=std)
    return render(request, 'students/std_detail.html', {
        'std': std,
        'disissue': disissue,
        'character_certificate': character_certificate,
    })

# edit class seven student detail


@ login_required
def edit_std_seven(request, std_code):
    class_teacher = StaffDetail.objects.filter(category='Teaching Staff')
    std = get_object_or_404(std_registration_form, pk=std_code)
    if request.method == 'POST':
        form = StdRegistration(request.POST, request.FILES, instance=std)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student detail updated successfully!')
            return render(request, 'students/edit_std.html', {'std': std, 'form': form, 'class_teacher': class_teacher})
        else:
            messages.error(request, 'Student detail update failed. Try again!')
            return render(request, 'students/edit_std.html', {'std': std, 'form': form, 'class_teacher': class_teacher})
    else:
        form = StdRegistration(instance=std)
        return render(request, 'students/edit_std.html', {'std': std, 'form': form, 'class_teacher': class_teacher})

# delete class seven student detail


@ login_required
def delete_std_seven(request, std_code):
    std = get_object_or_404(std_registration_form, pk=std_code)
    std.delete()
    return redirect('students:seven')


# class eight home page


def eight(request):
    male = std_registration_form.objects.filter(standard=8, gender='Male')
    female = std_registration_form.objects.filter(standard=8, gender='Female')
    total = std_registration_form.objects.filter(standard=8)
    all_field = std_registration_form.objects.filter(
        standard=8).order_by('name')
    myFilter = StudentFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 15)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'students/eight.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total
                   })
# class eight student detail


def std_detail_eight(request, std_code):
    std = get_object_or_404(std_registration_form, pk=std_code)
    disissue = DisciplinaryIssue.objects.filter(Student=std)
    character_certificate = CharacterCertificate.objects.filter(Student=std)
    return render(request, 'students/std_detail.html', {
        'std': std,
        'disissue': disissue,
        'character_certificate': character_certificate,
    })

# edit class eight student detail


@ login_required
def edit_std_eight(request, std_code):
    class_teacher = StaffDetail.objects.filter(category='Teaching Staff')
    std = get_object_or_404(std_registration_form, pk=std_code)
    if request.method == 'POST':
        form = StdRegistration(request.POST, request.FILES, instance=std)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student detail updated successfully!')
            return render(request, 'students/edit_std.html', {'std': std, 'form': form, 'class_teacher': class_teacher})
        else:
            messages.error(request, 'Student detail update failed. Try again!')
            return render(request, 'students/edit_std.html', {'std': std, 'form': form, 'class_teacher': class_teacher})
    else:
        form = StdRegistration(instance=std)
        return render(request, 'students/edit_std.html', {'std': std, 'form': form, 'class_teacher': class_teacher})

# delete class eight student detail


@ login_required
def delete_std_eight(request, std_code):
    std = get_object_or_404(std_registration_form, pk=std_code)
    std.delete()
    return redirect('students:eight')

# class nine home page


def nine(request):
    male = std_registration_form.objects.filter(standard=9, gender='Male')
    female = std_registration_form.objects.filter(standard=9, gender='Female')
    total = std_registration_form.objects.filter(standard=9)
    all_field = std_registration_form.objects.filter(
        standard=9).order_by('name')
    myFilter = StudentFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 15)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'students/nine.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total
                   })

# class nine student detail


def std_detail_nine(request, std_code):
    std = get_object_or_404(std_registration_form, pk=std_code)
    disissue = DisciplinaryIssue.objects.filter(Student=std)
    character_certificate = CharacterCertificate.objects.filter(Student=std)
    return render(request, 'students/std_detail.html', {
        'std': std,
        'disissue': disissue,
        'character_certificate': character_certificate,
    })

# edit class nine student detail


@ login_required
def edit_std_nine(request, std_code):
    class_teacher = StaffDetail.objects.filter(category='Teaching Staff')
    std = get_object_or_404(std_registration_form, pk=std_code)
    if request.method == 'POST':
        form = StdRegistration(request.POST, request.FILES, instance=std)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student detail updated successfully!')
            return render(request, 'students/edit_std.html', {'std': std, 'form': form, 'class_teacher': class_teacher})
        else:
            messages.error(request, 'Student detail update failed. Try again!')
            return render(request, 'students/edit_std.html', {'std': std, 'form': form, 'class_teacher': class_teacher})
    else:
        form = StdRegistration(instance=std)
        return render(request, 'students/edit_std.html', {'std': std, 'form': form, 'class_teacher': class_teacher})

# delete class nine student detail


@ login_required
def delete_std_nine(request, std_code):
    std = get_object_or_404(std_registration_form, pk=std_code)
    std.delete()
    return redirect('students:nine')

# class ten home page


def ten(request):
    male = std_registration_form.objects.filter(standard=10, gender='Male')
    female = std_registration_form.objects.filter(standard=10, gender='Female')
    total = std_registration_form.objects.filter(standard=10)
    all_field = std_registration_form.objects.filter(
        standard=10).order_by('name')
    myFilter = StudentFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 15)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'students/ten.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total
                   })

# class ten student detail


def std_detail_ten(request, std_code):
    std = get_object_or_404(std_registration_form, pk=std_code)
    disissue = DisciplinaryIssue.objects.filter(Student=std)
    character_certificate = CharacterCertificate.objects.filter(Student=std)
    return render(request, 'students/std_detail.html', {
        'std': std,
        'disissue': disissue,
        'character_certificate': character_certificate,
    })

# edit class ten student detail


@ login_required
def edit_std_ten(request, std_code):
    class_teacher = StaffDetail.objects.filter(category='Teaching Staff')
    std = get_object_or_404(std_registration_form, pk=std_code)
    if request.method == 'POST':
        form = StdRegistration(request.POST, request.FILES, instance=std)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student detail updated successfully!')
            return render(request, 'students/edit_std.html', {'std': std, 'form': form, 'class_teacher': class_teacher})
        else:
            messages.error(request, 'Student detail update failed. Try again!')
            return render(request, 'students/edit_std.html', {'std': std, 'form': form, 'class_teacher': class_teacher})
    else:
        form = StdRegistration(instance=std)
        return render(request, 'students/edit_std.html', {'std': std, 'form': form, 'class_teacher': class_teacher})

# delete class ten student detail


@ login_required
def delete_std_ten(request, std_code):
    std = get_object_or_404(std_registration_form, pk=std_code)
    std.delete()
    return redirect('students:ten')

# class eleven home page


def eleven(request):
    male = std_registration_form.objects.filter(standard=11, gender='Male')
    female = std_registration_form.objects.filter(standard=11, gender='Female')
    total = std_registration_form.objects.filter(standard=11)
    all_field = std_registration_form.objects.filter(
        standard=11).order_by('name')
    myFilter = StudentFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 15)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'students/eleven.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total
                   })

# class eleven student detail


def std_detail_eleven(request, std_code):
    std = get_object_or_404(std_registration_form, pk=std_code)
    disissue = DisciplinaryIssue.objects.filter(Student=std)
    character_certificate = CharacterCertificate.objects.filter(Student=std)
    return render(request, 'students/std_detail.html', {
        'std': std,
        'disissue': disissue,
        'character_certificate': character_certificate,
    })

# edit class eleven student detail


@ login_required
def edit_std_eleven(request, std_code):
    std = get_object_or_404(std_registration_form, pk=std_code)
    class_teacher = StaffDetail.objects.filter(category='Teaching Staff')
    if request.method == 'POST':
        form = StdRegistration(request.POST, request.FILES, instance=std)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student detail updated successfully!')
            return render(request, 'students/edit_std.html', {'std': std, 'form': form, 'class_teacher': class_teacher})
        else:
            messages.error(request, 'Student detail update failed. Try again!')
            return render(request, 'students/edit_std.html', {'std': std, 'form': form, 'class_teacher': class_teacher})
    else:
        form = StdRegistration(instance=std)
        return render(request, 'students/edit_std.html', {'std': std, 'form': form, 'class_teacher': class_teacher})

# delete class eleven student detail


@ login_required
def delete_std_eleven(request, std_code):
    std = get_object_or_404(std_registration_form, pk=std_code)
    std.delete()
    return redirect('students:eleven')

# class twelve home page


def twelve(request):
    male = std_registration_form.objects.filter(standard=12, gender='Male')
    female = std_registration_form.objects.filter(standard=12, gender='Female')
    total = std_registration_form.objects.filter(standard=12)
    all_field = std_registration_form.objects.filter(
        standard=12).order_by('name')
    myFilter = StudentFilter(request.GET, queryset=all_field)
    all_field = myFilter.qs
    paginator = Paginator(all_field, 15)
    page_number = request.GET.get('page')
    all_field = paginator.get_page(page_number)
    return render(request, 'students/twelve.html',
                  {'all_field': all_field,
                   'myFilter': myFilter,
                   'male': male,
                   'female': female,
                   'total': total
                   })

# class twelve student detail


def std_detail_twelve(request, std_code):
    std = get_object_or_404(std_registration_form, pk=std_code)
    disissue = DisciplinaryIssue.objects.filter(Student=std)
    character_certificate = CharacterCertificate.objects.filter(Student=std)
    return render(request, 'students/std_detail.html', {
        'std': std,
        'disissue': disissue,
        'character_certificate': character_certificate,
    })

# edit class twelve student detail


@ login_required
def edit_std_twelve(request, std_code):
    class_teacher = StaffDetail.objects.filter(category='Teaching Staff')
    std = get_object_or_404(std_registration_form, pk=std_code)
    if request.method == 'POST':
        form = StdRegistration(request.POST, request.FILES, instance=std)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student detail updated successfully!')
            return render(request, 'students/edit_std.html', {'std': std, 'form': form, 'class_teacher': class_teacher})
        else:
            messages.error(request, 'Student detail update failed. Try again!')
            return render(request, 'students/edit_std.html', {'std': std, 'form': form, 'class_teacher': class_teacher})
    else:
        form = StdRegistration(instance=std)
        return render(request, 'students/edit_std.html', {'std': std, 'form': form, 'class_teacher': class_teacher})

# delete class twelve student detail


@ login_required
def delete_std_twelve(request, std_code):
    std = get_object_or_404(std_registration_form, pk=std_code)
    std.delete()
    return redirect('students:twelve')
