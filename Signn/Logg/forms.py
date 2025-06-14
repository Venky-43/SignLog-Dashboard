from django import forms
from .models import Signup,Login

class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Signup
        fields = [
            'first_name', 'last_name', 'profile_picture', 'username',
            'email', 'password', 'confirm_password', 'address_line1',
            'city', 'state', 'pincode', 'user_type'
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'