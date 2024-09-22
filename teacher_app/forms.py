from django import forms
from auth_app.models import Teacher

class ImageForm(forms.Form):
    image = forms.ImageField(label='Choose a Picture', label_suffix='', widget=forms.FileInput(attrs={'class': 'image'}))

    def clean_image(self):
        image = self.cleaned_data['image']
        if not image:
            raise forms.ValidationError('You must upload an image')
        if image.size > 1024*1024*2:
            raise forms.ValidationError('Image size must be less than 2MB')
        return image

class TeacherEditForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'address','primary_number','secondary_number','dob','sex'
        ]
        widgets = {
            'dob': forms.TextInput(attrs={
                'disabled' : True
            }),
            'sex': forms.Select(attrs={
                'disabled' : True
            })
        }