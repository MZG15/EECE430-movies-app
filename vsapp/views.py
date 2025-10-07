from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse
#from django.template import loader
from .forms import CreateVideoForm, DeleteVideoForm, UpdateVideoIDForm
from .models import Video


def index(request):
	return render(request,'index.html')

def add_video(request):
	if request.method == 'POST':
		form = CreateVideoForm(request.POST)
		if form.is_valid():
			videoform = form.cleaned_data
			mi = videoform['MovieID']
			mt = videoform['MovieTitle']
			a1n = videoform['Actor1Name']
			a2n = videoform['Actor2Name']
			dn = videoform['DirectorName']  
			mg = videoform['MovieGenre']
			ry = videoform['ReleaseYear']
			Video.objects.create(MovieID=mi,MovieTitle=mt,Actor1Name=a1n,Actor2Name=a2n,DirectorName=dn,MovieGenre=mg,ReleaseYear=ry)
			return redirect('display_video')
	else:
		form = CreateVideoForm()
	V=Video.objects.all()
	return render(request, 'add_video.html', {'form': form,'V':V})

def display_video(request):
    form = CreateVideoForm()
    V=Video.objects.all()
    return render(request, 'display_video.html', {'form':form,'V':V})

def delete_video(request):
    if request.method == "POST":
        form = DeleteVideoForm(request.POST)
        if form.is_valid():
            movie_id = form.cleaned_data['MovieID']
            try:
                video = Video.objects.get(MovieID=movie_id)
                video.delete()
                return redirect('display_video')
            except Video.DoesNotExist:
                form.add_error('MovieID', "No video found with this ID")
    else:
        form = DeleteVideoForm()
    
    return render(request, 'delete_video.html', {'form': form})

def update_video(request):
    if request.method == "POST":
        if "MovieID" in request.POST and "MovieTitle" not in request.POST:
            # Step 1: user submitted an ID, show the update form
            id_form = UpdateVideoIDForm(request.POST)
            if id_form.is_valid():
                movie_id = id_form.cleaned_data['MovieID']
                try:
                    video = Video.objects.get(MovieID=movie_id)
                except Video.DoesNotExist:
                    id_form.add_error('MovieID', "No video found with this ID")
                    return render(request, 'update_video.html', {'id_form': id_form})
                
                form = CreateVideoForm(instance=video)
                return render(request, 'update_video.html', {'form': form, 'video': video})
        
        else:
            # Step 2: user submitted the edit form
            movie_id = request.POST.get("MovieID")
            try:
                video = Video.objects.get(MovieID=movie_id)
            except Video.DoesNotExist:
                return render(request, 'update_video.html', {
                    'id_form': UpdateVideoIDForm(),
                    'error': "⚠️ Video not found, cannot update."
                })
            form = CreateVideoForm(request.POST, instance=video)
            if form.is_valid():
                form.save()
                return redirect('display_video')  # back to video list
            return render(request, 'update_video.html', {'form': form, 'video': video})
    
    # GET request: show ID input form
    id_form = UpdateVideoIDForm()
    return render(request, 'update_video.html', {'id_form': id_form})
"""
def add_course(request):
	if request.method == 'POST':
		form = CreateCourseForm(request.POST)
		if form.is_valid():
			courseform = form.cleaned_data
			Student_id = courseform['Student_id']
			Course_id = courseform['Course_id']
			Semester = courseform['Semester']
			Number_of_credits = courseform['Number_of_credits']
			Grade = courseform['Grade']
			Course_Taken.objects.create(Student_id=Student_id,Course_id=Course_id,Semester=Semester,Number_of_credits=Number_of_credits,Grade=Grade)

			listing = Course_Taken.objects.filter(Student_id=Student_id)
			summ = 0.0
			credits = 0
			for l in listing:
				summ =summ+ l.Grade * l.Number_of_credits
				credits =credits+ l.Number_of_credits
			avg = summ / credits
			for e in Student.objects.all():
				if e.Student_id==Student_id:
					e.object.set(gpa=avg)
			return render(request, 'index.html')
	else:
		form = CreateCourseForm()
	S=Course_Taken.objects.all()
	return render(request, 'add_course.html', {'form': form,'S':S})
	

def report(request):
	if request.method == 'POST':
		form = GPAForm(request.POST)

		if form.is_valid():
			courseform = form.cleaned_data
			Student_id = courseform['Student_id']
						
			for e in Student.objects.all():
				if e.Student_id==Student_id:
					A=e
			return render(request, 'report_student.html', { 'form': form,'A':A})
		
	else:
		form= GPAForm()
	return render(request,'report_student.html',{'form':form})
"""