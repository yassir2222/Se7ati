from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User, Patient, Doctor, Article


class PatientSignUpForm(UserCreationForm):
   
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  

       
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5',
                'placeholder': field.label
            })
           
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm Password do not match."
            )

        return cleaned_data 

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'patient' 
        if commit:
            user.save()
            Patient.objects.create(user=user)
        return user


class DoctorSignUpForm(UserCreationForm):
    specialization = forms.CharField(max_length=255, label='Specialization')
    license_number = forms.CharField(max_length=50, label='License Number')
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply styling to standard fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5',
                'placeholder': field.label
            })

        
        self.fields['specialization'].widget.attrs.update({
            'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5',
            'placeholder': 'Specialization'
        })
        self.fields['license_number'].widget.attrs.update({
            'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5',
            'placeholder': 'License Number'
        })
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm Password do not match."
            )

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'doctor'  # Set the user type
        if commit:
            user.save()
            Doctor.objects.create(user=user, specialization=self.cleaned_data['specialization'],
                                  license_number=self.cleaned_data['license_number'])
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply styling to each field
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5',
                'placeholder': field.label
            })

        self.fields['username'].widget.attrs['placeholder'] = "Username"  # Specific placeholder
        self.fields['password'].widget.attrs['placeholder'] = "Password"  # Specific placeholder
    pass 

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5',
                'placeholder': field.label
            })
        self.fields['content'].widget = forms.Textarea(attrs={'rows': 5, 'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5', 'placeholder': 'Content'})