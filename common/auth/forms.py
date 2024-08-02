from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomSignupForm(SignupForm):
    phone_number = forms.CharField(max_length=15, required=False, label='Phone Number')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['username'].label = 'Username (변경 불가)'  # 레이블에 표시
        self.fields['username'].help_text = '이 필드는 변경할 수 없습니다.'  # 설명 추가
