from django.shortcuts import render, redirect

students = []
subjects = []
teachers = []
def dashboard(request):
    context = {
        "name": "John Doe",
        "role": "Admin",
        "students": students,
        "subjects": subjects,
        "teachers": teachers,
    }
    return render(request, 'backend/dashboard.html', context)

def add_student(request):

    if request.method == 'POST':

        if students:
            new_id = students[-1]["id"] + 1
        else:
            new_id = 1
        new_student = {
            "id": new_id,
            "last_name": request.POST.get('last_name'),
            "first_name": request.POST.get('first_name'),
            "gender": request.POST.get('gender'),
            "dob": request.POST.get('dob'),
            "address": request.POST.get('address'),
        }
        students.append(new_student)

        return redirect('dashboard')
    return render(request, 'backend/add_student.html')


def edit_student(request, id):

    student = None
    for s in students:
        if s["id"] == id:
            student = s

    # If someone clicked "Update"...
    if request.method == 'POST':
        student["last_name"] = request.POST.get('last_name')
        student["first_name"] = request.POST.get('first_name')
        student["gender"] = request.POST.get('gender')
        student["dob"] = request.POST.get('dob')
        student["address"] = request.POST.get('address')
        return redirect('dashboard')

    # Show the form with the student's info already filled in
    return render(request, 'backend/edit_student.html', {"student": student})


def delete_student(request, id):
    global students


    new_list = []
    for s in students:
        if s["id"] != id:
            new_list.append(s)
    students = new_list

    return redirect('dashboard')



def add_subject(request):
    if request.method == 'POST':

        if subjects:
            new_id = subjects[-1]["id"] + 1
        else:
            new_id = 1

        new_subject = {
            "id": new_id,
            "subject_name": request.POST.get('subject_name'),
        }
        subjects.append(new_subject)

        return redirect('dashboard')

    return render(request, 'backend/add_subject.html')


def edit_subject(request, id):
    subject = None
    for s in subjects:
        if s["id"] == id:
            subject = s

    if request.method == 'POST':
        subject["subject_name"] = request.POST.get('subject_name')
        return redirect('dashboard')

    return render(request, 'backend/edit_subject.html', {"subject": subject})


def delete_subject(request, id):
    global subjects

    new_list = []
    for s in subjects:
        if s["id"] != id:
            new_list.append(s)
    subjects = new_list

    return redirect('dashboard')


def add_teacher(request):
    if request.method == 'POST':

        if teachers:
            new_id = teachers[-1]["id"] + 1
        else:
            new_id = 1

        new_teacher = {
            "id": new_id,
            "last_name": request.POST.get('last_name'),
            "first_name": request.POST.get('first_name'),
            "gender": request.POST.get('gender'),
            "dob": request.POST.get('dob'),
            "address": request.POST.get('address'),
            "salary": request.POST.get('salary'),
        }
        teachers.append(new_teacher)

        return redirect('dashboard')

    return render(request, 'backend/add_teacher.html')


def edit_teacher(request, id):
    teacher = None
    for t in teachers:
        if t["id"] == id:
            teacher = t

    if request.method == 'POST':
        teacher["last_name"] = request.POST.get('last_name')
        teacher["first_name"] = request.POST.get('first_name')
        teacher["gender"] = request.POST.get('gender')
        teacher["dob"] = request.POST.get('dob')
        teacher["address"] = request.POST.get('address')
        teacher["salary"] = request.POST.get('salary')
        return redirect('dashboard')

    return render(request, 'backend/edit_teacher.html', {"teacher": teacher})


def delete_teacher(request, id):
    global teachers

    new_list = []
    for t in teachers:
        if t["id"] != id:
            new_list.append(t)
    teachers = new_list

    return redirect('dashboard')