from django import forms

from lesson_5.models import Client


class MyForm(forms.Form):
    name = forms.CharField(label="User name", initial="User name",
                           error_messages={'required': 'Please enter your'
                                                       ' available email'})
    profile_picture = forms.ImageField(widget=forms.FileInput, required=False)
    additional_file = forms.FileField(widget=forms.FileInput, required=False)
    email = forms.EmailField(initial="admin@admin.com", error_messages={
        'required': 'Please enter your available email'})
    password = forms.CharField(max_length=20, min_length=8,
                               required=False,
                               widget=forms.PasswordInput())
    age = forms.IntegerField(required=False, initial="45",
                             help_text="Enter your current age")
    agreement = forms.BooleanField(required=False)
    average_score = forms.FloatField(initial=10.1)
    birthday = forms.DateField(widget=forms.SelectDateWidget,
                               required=False)
    work_experience = forms.DurationField(required=False,)
    gender = forms.ChoiceField(required=False,
                               choices=[("1", "man"), ("2", "woman"), ('3', 'child')])


class FormFromModel(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
