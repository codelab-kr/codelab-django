from django import forms
from django.contrib.auth import get_user_model

from services.courses.models import Course

# from django.contrib.auth.forms import UserCreationForm

CustomUser = get_user_model()

# class StudentRegistrationForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')  # 원하는 필드를 추가/수정할 수 있습니다.


class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.HiddenInput)
