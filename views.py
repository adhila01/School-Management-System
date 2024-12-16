from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render,redirect


from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
# Create your views here.
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("registration success")  # Redirect to a success page
    else:
        form = StudentRegistrationForm()
    return render(request, 'register.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import Student

def login_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            student = Student.objects.get(name=name)
        except Student.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid name or password'})

        # Check if the password is correct
        if check_password(password, student.password):
            # Save student info in session (optional)
            request.session['student_id'] = student.id
            request.session['student_name'] = student.name
            return redirect('userprofile') # Redirect to a dashboard or success page
        else:
            return render(request, 'login.html', {'error': 'Invalid name or password'})

    return render(request, 'login.html')

def logout_student(request):
    request.session.flush()  # Clear session data
    return redirect('login')

# def dashboard(request):
#     if 'student_id' not in request.session:
#         return redirect('login')  # Redirect to login if not logged in
#     return render(request, 'dashboard.html', {'student_name': request.session['student_name']})


from django.shortcuts import render, redirect
from .models import Student

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Student

@login_required
# def profile_view(request):
#     # Fetch the logged-in user's Student details
#     student = Student.objects.get(user=request.user)
#     return render(request, 'profile.html', {'student': student})
def userprofile(request):
    try:
      category=request.GET.get('category','all')#get selecetd category,if there is no category all option  will work
      id1=request.session['userid']  #session calling
      data=Student.objects.get(id=id1)
      if category == 'all':
        db=login_student.objects.all()
      else:
        db=Student.objects.filter(category=category)
    # pre-process the size data
      for item in db:
         item.sizes = item.sizes.split(',')
      return render (request, 'profile.html',{'data':data,'db':db })
    except KeyError:
        return redirect(login_student)

