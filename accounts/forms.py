from django import forms
from .models import account, Profile
from django.contrib.auth.forms import PasswordChangeForm

class RegistrationForm(forms.ModelForm):
    # this code added password and confirm_password to the form fields with some css
    password = forms.CharField(widget=forms.PasswordInput(attrs= {
        'placeholder': 'Enter password',
    }, ))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs= {
        'placeholder': 'Confirm password',
    }, ),)
    # the meta tells django how to display this form fields
    class Meta:
        model = account
        fields = ['first_name','last_name', 'email', 'phone_number','password',]
    #this code added some css to my model form display on the front end
    def __init__(self, *args, **kwargs ):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']= 'Enter First name'
        self.fields['last_name'].widget.attrs['placeholder']= 'Enter last name'
        self.fields['phone_number'].widget.attrs['placeholder']= 'Enter Enter phone Number'
        self.fields['email'].widget.attrs['placeholder']= 'Enter Email'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class']= 'form-control'

# this code will bring my form data to lowercase ie the email , so that when a user types in any case , it will be accepted
    def clean_email(self):
        data = self.cleaned_data['email']
        return data.lower()
    
   # this code confirms that password and confirm-password are matched if not , it gives u an error
    def clean(self):
        cleaned_data = super(RegistrationForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                ' password does not match'
            )





class EditProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['bio', 'profile_image', 'date_birth', 'nationality', 'state', 'address','profession']  # Add any other fields you want to include

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    

# forms.py

from django import forms
from .models import Profile

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']  # Only include the profile_picture field
