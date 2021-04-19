from django.shortcuts import render,redirect
from .forms import StudentForm  
from .models import Student

# Create your views here.
def homepage(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('/show')  
            
    else:  
        form = StudentForm()  
    return render(request,'crudapp/index.html',{'form':form})  

def show(request):  
    students = Student.objects.all()  
    return render(request,"crudapp/show.html",{'students':students})  

def edit(request, id):  
    student = Student.objects.get(id=id)  
    return render(request,'crudapp/edit.html', {'student':student})  

def update(request, id):  
    student = Student.objects.get(id=id)  
    form     = StudentForm(request.POST, instance = student)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'crudapp/edit.html', {'student': student})  

def destroy(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()  
    return redirect("/show")  