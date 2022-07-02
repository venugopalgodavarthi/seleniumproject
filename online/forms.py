from django import forms
from online.models import universitymodel, collegemodel


class universityform(forms.ModelForm):
    class Meta:
        model = universitymodel
        fields = '__all__'


class collegeform(forms.ModelForm):
    class Meta:
        model = collegemodel
        fields = '__all__'
