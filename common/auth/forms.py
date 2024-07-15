from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User


class SignUp(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id-register'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout('username', 'email', 'phone_number', 'password1', 'password2')

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')
        field_classes = {'username': UsernameField}


class Login(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id-register'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            'username',
            'password',
        )


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('이미 사용 중인 이메일 주소입니다.')
        return data


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError('이미 사용 중인 이메일 주소입니다.')
        return data


# class ProfileEditForm(forms.ModelForm):

#     class Meta:
#         model = Profile
#         fields = ['date_of_birth', 'photo']
