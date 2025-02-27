from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from base.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','profile_pic','website_link','facebook_link','ig_link','X')
        widget ={
                'bio': forms.Textarea(attrs={'class':'form-control'}),
                #'Profile_pic': forms.TextInput(attrs={'class':'form-control'}),
                'website_link': forms.TextInput(attrs={'class':'form-control'}),
                'facebook_link': forms.TextInput(attrs={'class':'form-control'}),
                'ig_link': forms.TextInput(attrs={'class':'form-control'}),
                'X': forms.TextInput(attrs={'class':'form-control'}),
        }
        


class SingUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args,  **kwargs):
        super(SingUpForm, self).__init__(*args,  **kwargs)

        self.fields ['username'].widget.attrs['class'] = 'form-control'
        self.fields ['password1'].widget.attrs['class'] = 'form-control'
        self.fields ['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    is_superuser = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_staff = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password','last_login','is_superuser','is_staff','is_active','date_joined')

    
    
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.EmailField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1 = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2 = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    
    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2',)


