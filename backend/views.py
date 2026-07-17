from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Student, Subject, Teacher


def dashboard(request):
    context = {
        "name": "John Doe",
        "role": "Admin",
        "students": Student.objects.all(),
        "subjects": Subject.objects.all(),
        "teachers": Teacher.objects.all(),
    }
    return render(request, 'backend/dashboard.html', context)


# ---------- STUDENTS ----------
def student_list(request):
    q = request.GET.get('q', '')
    students = Student.objects.all()
    if q:
        students = students.filter(
            Q(first_name__icontains=q) | Q(last_name__icontains=q)
        )
    return render(request, 'backend/student_list.html', {"students": students, "q": q})


def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            last_name=request.POST.get('last_name'),
            first_name=request.POST.get('first_name'),
            gender=request.POST.get('gender'),
            dob=request.POST.get('dob') or None,
            address=request.POST.get('address'),
        )
        return redirect('student_list')
    return render(request, 'backend/add_student.html')


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.last_name = request.POST.get('last_name')
        student.first_name = request.POST.get('first_name')
        student.gender = request.POST.get('gender')
        student.dob = request.POST.get('dob') or None
        student.address = request.POST.get('address')
        student.save()
        return redirect('student_list')
    return render(request, 'backend/edit_student.html', {"student": student})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')


# ---------- SUBJECTS ----------
def subject_list(request):
    q = request.GET.get('q', '')
    subjects = Subject.objects.all()
    if q:
        subjects = subjects.filter(subject_name__icontains=q)
    return render(request, 'backend/subject_list.html', {"subjects": subjects, "q": q})


def add_subject(request):
    if request.method == 'POST':
        Subject.objects.create(subject_name=request.POST.get('subject_name'))
        return redirect('subject_list')
    return render(request, 'backend/add_subject.html')


def edit_subject(request, id):
    subject = get_object_or_404(Subject, id=id)
    if request.method == 'POST':
        subject.subject_name = request.POST.get('subject_name')
        subject.save()
        return redirect('subject_list')
    return render(request, 'backend/edit_subject.html', {"subject": subject})


def delete_subject(request, id):
    subject = get_object_or_404(Subject, id=id)
    subject.delete()
    return redirect('subject_list')


# ---------- TEACHERS ----------
def teacher_list(request):
    q = request.GET.get('q', '')
    teachers = Teacher.objects.all()
    if q:
        teachers = teachers.filter(
            Q(first_name__icontains=q) | Q(last_name__icontains=q)
        )
    return render(request, 'backend/teacher_list.html', {"teachers": teachers, "q": q})


def add_teacher(request):
    if request.method == 'POST':
        Teacher.objects.create(
            last_name=request.POST.get('last_name'),
            first_name=request.POST.get('first_name'),
            gender=request.POST.get('gender'),
            dob=request.POST.get('dob') or None,
            address=request.POST.get('address'),
            salary=request.POST.get('salary') or None,
        )
        return redirect('teacher_list')
    return render(request, 'backend/add_teacher.html')


def edit_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == 'POST':
        teacher.last_name = request.POST.get('last_name')
        teacher.first_name = request.POST.get('first_name')
        teacher.gender = request.POST.get('gender')
        teacher.dob = request.POST.get('dob') or None
        teacher.address = request.POST.get('address')
        teacher.salary = request.POST.get('salary') or None
        teacher.save()
        return redirect('teacher_list')
    return render(request, 'backend/edit_teacher.html', {"teacher": teacher})


def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    teacher.delete()
    return redirect('teacher_list')