from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    date_of_birth = forms.DateField(required=False)
    address = forms.CharField(required=False)
    zip_code = forms.CharField(max_length = 10)
    location = forms.CharField(required=False)
    phone_number = forms.CharField(required=False)
    mobile_number = forms.CharField(required=False)
