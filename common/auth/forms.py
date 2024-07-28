from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    phone_number = forms.CharField(max_length=15, required=False, label='Phone Number')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user