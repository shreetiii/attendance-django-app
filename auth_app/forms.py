from django import forms
import re  

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input', 'maxlength' :'100' , 'placeholder' : 'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'input', 'maxlength' :'50', 'placeholder' : 'Enter Password'}))

    # def clean_username(self):
    #     uname = self.cleaned_data.get('username')
    #     if len(uname) <= 5 and ' ' in uname:
    #         raise forms.ValidationError('Username must be more than 5 characters and should not contain spaces')
    #     return uname
    
    # def clean_password(self):
    #     pwd = self.cleaned_data.get('password')
    #     if '$' not in pwd:
    #         raise forms.ValidationError('Password Must Contain $')
    #     return pwd


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' : 'Enter Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Confirm Password'}))

    def clean_first_name(self):
        fname = self.cleaned_data.get('first_name')
        if not fname.isalpha():
            raise forms.ValidationError('First Name should contain only alphabets')
        return fname
    
    def clean_last_name(self):
        lname = self.cleaned_data.get('last_name')
        if not lname.isalpha():
            raise forms.ValidationError('Last Name should contain only alphabets')
        return lname
    
    def clean_username(self):
        uname = self.cleaned_data.get('username')
        if len(uname) <= 5 and ' ' in uname:
            raise forms.ValidationError('Username must be more than 5 characters')
        return uname

    def clean_password1(self):
        pwd1 = self.cleaned_data.get('password1')
        if len(pwd1) < 8:
            raise forms.ValidationError('Password must be more than 8 characters')
        if not re.search('[A-Z]',pwd1):
            raise forms.ValidationError('Password must contain at least 1 uppercase letter')
        if not re.search('[a-z]',pwd1):
            raise forms.ValidationError('Password must contain at least 1 uppercase letter')
        if not re.search('[0-9]',pwd1):
            raise forms.ValidationError('Password must contain at least 1 digit')
        if not re.search('[\W*]',pwd1):
            raise forms.ValidationError('Password must contain at least 1 special character')
        
        return pwd1