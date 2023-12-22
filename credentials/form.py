# forms.py
from select import select
from django import forms
from .models import Order, Department, Course, Purpose, Material

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'department': forms.Select(attrs={"hx-get":"/credentials/loadcourse/","hx-target":"#id_courses"}),
            'course': forms.Select(),
            'purpose': forms.Select(),
            'materials_provide': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        # Dynamically load courses based on selected department using JavaScript
        self.fields['department'].widget.attrs.update({"hx-get":"/loadcourse/","hx-target":"#id_courses"})

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'department']

        
class SubjectForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all(),
     widget=forms.Select(attrs={"hx-get":"loadcourse","hx-target":"#id_courses"})) 
    # widget=forms.Select(attrs={"hx-get": "loadcourse/", "hx-target": "#id_courses"})
    # )
    courses = forms.ModelChoiceField(queryset=Course.objects.none())
    
    
class PurposeForm(forms.ModelForm):
    class Meta:
        model = Purpose
        fields = ['name']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name']
