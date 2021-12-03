from django import forms

from employee.models import Employers, Department, ProgrammingLanguage


class EmployersForm(forms.ModelForm):
    class Meta:
        model = Employers
        fields = "__all__"


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class ProgrammingLanguageForm(forms.ModelForm):
    class Meta:
        model = ProgrammingLanguage
        fields = "__all__"
