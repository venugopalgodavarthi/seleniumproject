from django import forms


def first(name):
    if not(name[0].isupper()):
        raise forms.ValidationError(
            "firstname startwith uppercase character")
    if not(name.isalpha()):
        raise forms.ValidationError(
            "firstname should be Alphabets")


class sampleform(forms.Form):

    firstname = forms.CharField(max_length=15, min_length=3,
                                required=True, label="first_name",
                                help_text="plz enter the value",
                                widget=forms.TextInput(
                                    attrs={'placeholder': "first_name"}),
                                validators=[first])
    age = forms.IntegerField(max_value=85, min_value=10)

    '''
    def clean(self):
        name = self.cleaned_data['firstname']
        if not(name[0].isupper()):
            raise forms.ValidationError(
                "firstname startwith uppercase character")
        if not(name.isalpha()):
            raise forms.ValidationError(
                "firstname should be Alphabets")

    def clean_firstname(self):
        name = self.cleaned_data['firstname']
        if not(name[0].isupper()):
            raise forms.ValidationError(
                "firstname startwith uppercase character")
        if not(name.isalpha()):
            raise forms.ValidationError(
                "firstname should be Alphabets")
        return name
    '''
    '''
    name = forms.CharField()
    name1 = forms.CharField(widget=forms.TextInput)
    name2 = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 10}))
    name3 = forms.CharField(widget=forms.EmailInput)
    name4 = forms.CharField(widget=forms.DateInput)
    name5 = forms.CharField(widget=forms.PasswordInput)
    name6 = forms.CharField(widget=forms.HiddenInput)
    name6 = forms.CharField(widget=forms.FileInput)
    name7 = forms.CharField(widget=forms.SelectDateWidget)
    name8 = forms.CharField(widget=forms.TimeInput)
    name9 = forms.CharField(widget=forms.DateTimeInput)

    g = [['male', 'Male'], ['female', 'Female'], ['others', 'others']]
    gender = forms.ChoiceField(choices=g)

    gender1 = forms.ChoiceField(choices=g, widget=forms.RadioSelect)

    g = [['red', 'red'], ['green', 'green'], ['blue', 'blue']]
    gender2 = forms.MultipleChoiceField(choices=g)

    gender3 = forms.MultipleChoiceField(
        choices=g, widget=forms.CheckboxSelectMultiple)
    '''
