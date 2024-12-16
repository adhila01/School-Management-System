from django import forms
from .models import Student
from django.contrib.auth.hashers import make_password

class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['name', 'student_class', 'division', 'password']

    def save(self, commit=True):
        student = super().save(commit=False)
        student.password = make_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            student.save()
        return student
