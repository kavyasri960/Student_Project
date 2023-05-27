from students.models import Students1
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def insertData(request):
    #return render(request,'studentform.html');
    if request.method == 'POST':
        if request.POST.get('Student_id') and request.POST.get('Student_Name') and request.POST.get('Student_TotalMarks') :
            toBeSaved = Students1();
            toBeSaved.Student_id = request.POST.get('Student_id');
            toBeSaved.Student_Name = request.POST.get('Student_Name');
            toBeSaved.Student_TotalMarks = request.POST.get('Student_TotalMarks');
            toBeSaved.save();
            messages.success(request,'Your changes are saved successfully');
            return render(request, 'studentform.html')
    else:
        return render(request, 'studentform.html')        

    





    












