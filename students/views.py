from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Student
from .forms import StudentForm

def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })

def view_student(request, id):
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        raise Http404("Student not found")
    return redirect('index')

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True
            })
        else:
            return render(request, 'students/add.html', {
                'form': form
            })

    form = StudentForm()
    return render(request, 'students/add.html', {
        'form': form
    })

def edit(request, id):
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        raise Http404("Student not found")

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True
            })
        else:
            return render(request, 'students/edit.html', {
                'form': form
            })

    form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {
        'form': form
    })

def delete(request, id):
    try:
        student = Student.objects.get(pk=id)
        student.delete()
    except Student.DoesNotExist:
        raise Http404("Student not found")
    return HttpResponseRedirect(reverse('index'))
